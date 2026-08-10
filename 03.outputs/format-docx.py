#!/usr/bin/env python3
"""Post-render formatting for the rendered docx.

Quarto's docx writer cannot express these requirements, so they are applied to
the output file after render, never to the reference doc, which is a verified
artifact. The rules, from the 10 August request: code blocks at 8 pt, left
aligned, single spaced with no gap before or after so they sit as compact as
the page allows; every data table 16.5 cm wide with cells left justified at
8 pt and the header row bold and centred. The spacing override matters because
the submission reference doc sets true double spacing in its defaults, which
code blocks would otherwise inherit.

The docx wraps each captioned table in a 1x1 outer table holding the caption
and the inner data table; figures use the same wrapper with an image instead,
so a wrapper is treated as a data table only when it contains an inner table.
Pandoc emits duplicated w:jc elements inside one w:pPr, so every existing jc
is removed before python-docx sets the intended alignment, otherwise Word
keeps whichever it read first.

tblW and tblLayout are inserted in the schema's child order rather than
appended. An earlier draft appended them after tblLook, which Word opens only
through its repair dialog, and a submission file must never risk that.

Usage: python3 format-docx.py <file.docx>
"""

import sys

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Pt

TABLE_W_DXA = 9355          # 16.5 cm in twentieths of a point
CELL_MARGIN_DXA = 108       # Word default table cell margin, each side
FONT_SIZE = Pt(8)

# CT_TblPr child sequence from the OOXML schema; insertion respects it.
TBLPR_SEQ = (
    "w:tblStyle", "w:tblpPr", "w:tblOverlap", "w:bidiVisual",
    "w:tblStyleRowBandSize", "w:tblStyleColBandSize", "w:tblW", "w:jc",
    "w:tblCellSpacing", "w:tblInd", "w:tblBorders", "w:shd", "w:tblLayout",
    "w:tblCellMar", "w:tblLook", "w:tblCaption", "w:tblDescription",
    "w:tblPrChange",
)


def set_tblpr_child(tblPr, tag, attrs):
    for el in tblPr.findall(qn(tag)):
        tblPr.remove(el)
    el = tblPr.makeelement(qn(tag), {qn(k): v for k, v in attrs.items()})
    successors = TBLPR_SEQ[TBLPR_SEQ.index(tag) + 1:]
    tblPr.insert_element_before(el, *successors)


def set_tbl_width(tbl, dxa):
    set_tblpr_child(tbl.tblPr, "w:tblW", {"w:type": "dxa", "w:w": str(dxa)})
    set_tblpr_child(tbl.tblPr, "w:tblLayout", {"w:type": "fixed"})
    grid = tbl.find(qn("w:tblGrid"))
    cols = grid.findall(qn("w:gridCol")) if grid is not None else []
    if cols:
        widths = [int(c.get(qn("w:w")) or 0) for c in cols]
        if not sum(widths):
            widths = [1] * len(cols)
        total = sum(widths)
        scaled = [dxa * w // total for w in widths]
        scaled[-1] += dxa - sum(scaled)
        for c, w in zip(cols, scaled):
            c.set(qn("w:w"), str(w))


def set_par_alignment(p, alignment):
    pPr = p._p.get_or_add_pPr()
    for el in pPr.findall(qn("w:jc")):
        pPr.remove(el)
    p.alignment = alignment


def set_par_compact(p):
    pPr = p._p.get_or_add_pPr()
    for el in pPr.findall(qn("w:spacing")):
        pPr.remove(el)
    fmt = p.paragraph_format
    fmt.line_spacing = 1.0
    fmt.space_before = Pt(0)
    fmt.space_after = Pt(0)


def format_data_table(table):
    set_tbl_width(table._tbl, TABLE_W_DXA - 2 * CELL_MARGIN_DXA)
    for i, row in enumerate(table.rows):
        header = i == 0
        for cell in row.cells:
            for p in cell.paragraphs:
                set_par_alignment(
                    p, WD_ALIGN_PARAGRAPH.CENTER if header else WD_ALIGN_PARAGRAPH.LEFT)
                for run in p.runs:
                    run.font.size = FONT_SIZE
                    if header:
                        run.font.bold = True


def main(path):
    doc = docx.Document(path)
    data_tables = 0
    for wrapper in doc.tables:
        inner_tables = [t for r in wrapper.rows for c in r.cells for t in c.tables]
        if not inner_tables:
            continue  # figure wrapper, leave untouched
        set_tbl_width(wrapper._tbl, TABLE_W_DXA)
        for inner in inner_tables:
            format_data_table(inner)
            data_tables += 1
    code_pars = 0
    for p in doc.paragraphs:
        if p.style.name == "Source Code":
            set_par_alignment(p, WD_ALIGN_PARAGRAPH.LEFT)
            set_par_compact(p)
            for run in p.runs:
                run.font.size = FONT_SIZE
            code_pars += 1
    doc.save(path)
    print(f"{path}: {data_tables} data tables set to 16.5 cm, 8 pt, "
          f"left cells, bold centred header; {code_pars} code blocks at "
          f"8 pt left, single spaced")


if __name__ == "__main__":
    main(sys.argv[1])
