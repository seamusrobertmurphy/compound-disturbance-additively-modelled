#!/usr/bin/env python3
"""Rebuild the repository README from the rendered manuscript.

The README carries the abstract and then every rendered output, figures and
tables interleaved in the order they appear in the manuscript, all taken from
the current render rather than retyped so the two cannot drift. Rerun after any
`quarto render`:

    python3 03.outputs/build-readme.py

Three things this script exists to handle:

1. GitHub does not render the Pandoc grid tables Quarto produces, so a paste of
   the render would print a wall of plus signs. Tables are converted to HTML
   tables, with column alignment preserved.
2. Figures are decoded from the HTML render's embedded base64, which keeps them
   in document order and avoids picking up the Word reference template's own
   images.
3. Every table and figure is standardised to span the full README column, per
   the 10 August request. GitHub's stylesheet sizes tables to their content
   (width: max-content, capped at max-width: 100%), strips style attributes,
   and ignores a width attribute on the table element itself, so pipe tables
   cannot be widened. Pixel width hints on header cells do enter the
   max-content computation, so each table carries per-column hints that sum
   well past the column width and the cap clamps every table to exactly 100
   per cent. If GitHub ever neutralises the hints the tables fall back to
   content-sized, which is today's appearance, not something worse. Figures
   get width="100%" for the same uniformity.
"""
import base64
import html
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "01.manuscript" / "compound-disturbance-additively-modelled.html"
QMD = ROOT / "01.manuscript" / "compound-disturbance-additively-modelled.qmd"
FIGDIR = ROOT / "03.outputs" / "PNG"
OUT = ROOT / "README.md"

MIN_FIG_WIDTH = 1000  # anything narrower is interface furniture, not a figure


def clean(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def front_matter() -> dict:
    """Pull title, subtitle and abstract from the qmd front matter.

    Read from the source rather than hardcoded, so editing the manuscript's
    title or framing cannot leave the README asserting the old one.
    """
    body = QMD.read_text(encoding="utf8").split("---", 2)[1]
    out, key, buf = {}, None, []
    for line in body.splitlines():
        m = re.match(r"^(title|subtitle|abstract):\s*(.*)$", line)
        if m:
            if key:
                out[key] = " ".join(buf).strip()
            key, buf = m.group(1), []
            rest = m.group(2).strip()
            if rest and rest != ">":
                buf.append(rest.strip('"').strip("'"))
            continue
        if key:
            if line and not line[0].isspace():
                out[key] = " ".join(buf).strip()
                key, buf = None, []
                continue
            buf.append(line.strip())
    if key:
        out[key] = " ".join(buf).strip()
    return {k: re.sub(r"\s+", " ", v).strip() for k, v in out.items()}


# Width hints sum to twice a comfortable README column so the max-width cap
# clamps every table to exactly the full column, whatever the viewer's window.
HINT_TOTAL = 2400
HINT_MIN = 90


def to_html_table(chunk: str) -> str | None:
    m = re.search(r"<table[^>]*>(.*?)</table>", chunk, re.S)
    if not m:
        return None
    tb = m.group(1)
    head = re.search(r"<thead>(.*?)</thead>", tb, re.S)
    body = re.search(r"<tbody>(.*?)</tbody>", tb, re.S)
    if not head or not body:
        return None
    heads = [clean(c) for c in re.findall(r"<th[^>]*>(.*?)</th>", head.group(1), re.S)]
    aligns = []
    for attrs in re.findall(r"<th([^>]*)>", head.group(1)):
        if "text-align: right" in attrs:
            aligns.append("right")
        elif "text-align: center" in attrs:
            aligns.append("center")
        else:
            aligns.append("left")
    rows = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", body.group(1), re.S):
        cells = [clean(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
        if cells:
            rows.append(cells)
    if not heads or not rows:
        return None
    while len(aligns) < len(heads):
        aligns.append("left")
    rows = [(r + [""] * len(heads))[: len(heads)] for r in rows]

    # Column hints proportional to the longest content in each column, so the
    # clamp preserves the proportions a content-sized table would have had.
    longest = [max([len(h)] + [len(r[i]) for r in rows]) for i, h in enumerate(heads)]
    total = sum(max(n, 4) for n in longest)
    hints = [max(HINT_MIN, round(HINT_TOTAL * max(n, 4) / total)) for n in longest]

    esc = html.escape
    out = ["<table>", "<thead>", "<tr>"]
    for h, a, w in zip(heads, aligns, hints):
        out.append(f'<th align="{a}" width="{w}">{esc(h)}</th>')
    out += ["</tr>", "</thead>", "<tbody>"]
    for r in rows:
        out.append("<tr>" +
                   "".join(f'<td align="{a}">{esc(c)}</td>' for c, a in zip(r, aligns)) +
                   "</tr>")
    out += ["</tbody>", "</table>"]
    return "\n".join(out)


def save_figure(chunk: str, slug: str) -> Path | None:
    for b64 in re.findall(r'<img[^>]*src="data:image/png;base64,([^"]+)"', chunk):
        data = base64.b64decode(b64)
        width = struct.unpack(">I", data[16:20])[0]
        if width < MIN_FIG_WIDTH:
            continue
        FIGDIR.mkdir(parents=True, exist_ok=True)
        path = FIGDIR / f"{slug}.png"
        path.write_bytes(data)
        return path.relative_to(ROOT)
    return None


def main() -> None:
    doc = HTML.read_text(encoding="utf8")

    # Every float, in the order it appears in the document.
    floats = [(m.start(), m.group(1)) for m in
              re.finditer(r'<div id="((?:tbl|fig)-[^"]+)"', doc)]
    bounds = [p for p, _ in floats] + [len(doc)]

    fm = front_matter()
    parts = [
        f"# {fm.get('title', 'Manuscript')}",
        "",
        f"*{fm['subtitle']}*" if fm.get("subtitle") else "",
        "",
        "Generated from the rendered manuscript by `03.outputs/build-readme.py`. "
        "Do not edit this file by hand: edit "
        "`01.manuscript/compound-disturbance-additively-modelled.qmd`, render, then rerun the script.",
        "",
        "## Abstract",
        "",
        fm.get("abstract", ""),
        "",
        "## Results",
        "",
        "Every figure and table below is reproduced from the current render, "
        "in the order it appears in the manuscript.",
        "",
    ]

    n_fig = n_tbl = 0
    for i, (start, slug) in enumerate(floats):
        chunk = doc[start:bounds[i + 1]]
        cap = ""
        for c in re.findall(r"<figcaption[^>]*>(.*?)</figcaption>", chunk, re.S):
            c = clean(c)
            if re.match(r"^(Table|Figure) \d+:", c):
                cap = c
                break
        label, _, text = cap.partition(":")
        label, text = label.strip(), text.strip()

        if slug.startswith("fig-"):
            path = save_figure(chunk, slug)
            if not path:
                continue
            n_fig += 1
            parts += [f"### {label or 'Figure'}", "",
                      f'<img src="{path.as_posix()}" alt="{label}" width="100%">',
                      "", f"*{text}*", ""]
        else:
            table = to_html_table(chunk)
            if not table:
                continue
            n_tbl += 1
            parts += [f"### {label or 'Table'}", "", f"*{text}*", "", table, ""]

    OUT.write_text("\n".join(parts).rstrip() + "\n", encoding="utf8")
    print(f"wrote {OUT.relative_to(ROOT)}: {n_fig} figures and {n_tbl} tables, in document order")


if __name__ == "__main__":
    main()
