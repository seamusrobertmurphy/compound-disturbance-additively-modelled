# Task request: compound beetle and fire disturbance at Darkwoods

**Date:** 2 August 2026
**For:** a fresh session, in a fresh repository, with no prior context
**Parent paper:** Murphy et al. 2026, FORECO-D-26-01171, *Forest Ecology and Management*, published

**Sibling paper, and the template for everything here:**
`/Volumes/PortableSSD/Github/claude-science-library/publications-academic/beetle-topography-and-wind-study/`
Full executable draft, renders end to end. Copy its structure, its conventions and its house rules.
Read its `INDEX.md` first, then `05.tasks/progress.md`, then the `.qmd` itself. Repository:
`https://github.com/seamusrobertmurphy/beetle-topography-and-wind-study`
**Status of this document:** scoping complete, data verified on disk, awaiting the author's go-ahead

**Working title, chosen by the author on 2 August 2026:**

> **Compound disturbance, additively modelled**
> *Testing whether beetle mortality and fire severity interact, in the landscape and in the model,
> Darkwoods Conservation Area, British Columbia*

**Project name:** `beetle-fire-compound-disturbance`

The title is deliberately outcome-neutral and survives every result this study can produce. If the
interaction is real it describes what was tested; if it is null, or if trap 1 in §6 shows the
association is an artefact of clipping, the title still holds and the paper becomes an account of
compound-disturbance claims outrunning the models fitted to support them. **Do not change it to
assert a finding before §7 Phase 2 has run.**

---

## 1. Read this first

This is the third paper in a family. The first is published. The second is drafted. This is the
third, and it has not been started. Everything below was verified by running code against the
actual rasters on 2 August 2026, not inferred from notes. Where something is unverified this
document says so.

**The one-sentence pitch.** The published paper is titled *A point process model of disturbance
interactions* and its abstract describes "the additive effects of increasing beetle-fire disturbance
interactions", but it never tested an interaction: beetle and fire enter its model as additive main
effects, and it never asked how the two agents relate to each other on the ground. This paper asks
both questions, using data that was built in 2021 and never used.

## 2. What changed during scoping, and why the plan is not what was first proposed

The original recommendation was **cross-agent spectral separability**: can the burn signal (NBR) and
the red-attack signal (NDMI) be told apart from each other where the two disturbances overlap? That
was the 13 June 2026 scoping memo's own recommended anchor
(`Archive/writing_outputs/20260613_053044_rs_methods_spinoff/PHASE0_Scoping_Novelty_Memo.md`,
line 50).

**It is not feasible from local data, and that is a firm finding.** A separability analysis needs the
continuous spectral surfaces for both agents. On disk:

| Surface | State | Consequence |
|---|---|---|
| `fire_severity/NDBR1.tif` | **Classified**, 5 values (0, 1, 16, 32, 34) | No continuous dNBR |
| `fire_severity/Fire.Severity.NDBR.tif` | **Classified**, same 5 values | No continuous dNBR |
| `beetle_stages/MPB.classified.spatstat.tif` | **Continuous**, -0.175 to 0.009, 82 unique values | Beetle side survives |
| Landsat bands, NDMI, tasselled-cap rasters | **Absent** | Nothing to recompute from |

So one agent has a continuous surface and the other does not. Running the separability analysis would
mean re-acquiring the Landsat archive and re-deriving the indices, which is both a large amount of
work and a re-tread of the published methods, which is the dual-publication problem this whole family
of spin-offs exists to avoid. **Do not start there.** It is recorded in §8 as optional future work.

What replaced it is better: two interaction questions that are feasible today with data already on
disk, and that the published paper's own framing most needs.

## 3. The contribution

Two questions, one paper.

**Question A. Did prior beetle mortality shape subsequent burn severity?**
The beetle outbreak ran 2005 to 2014. The fire burned in 2015. The causal arrow therefore runs
beetle to fire, and the question is whether stands carrying red-attack mortality burned differently
from stands that did not. This is a contested literature (Meigs, Harvey, Talucci, Hart, Simard), so
novelty rests on the specific landscape and on the honesty of the confound treatment, not on the
question being new.

**Question B. Do beetle and fire act additively on regeneration, or do they interact?**
The published model fits

```
Y_i = exp(b1 SSdist + b2 RA + b3 GA + b4 + BS + b5 RIX + b6 AS + b7 W + e_i)
```

with red-attack (RA), grey-attack (GA) and burn severity (BS) as **additive main effects and no
product term**, while the paper is titled and framed around interactions. Refitting with the
interaction term is the direct test. The author's own figure note flagged this ambiguity at the time
(`5.Submissions/Archive/Figures_FEM_Submission/compound_disturbance_analysis.md`, lines 67 to 76):
"'additive effects' could mean: the effects simply add together (1 + 1 = 2) OR the combined effect is
the sum of individual effects."

**Why the two belong together.** A asks whether the agents interact in the landscape; B asks whether
they interact in their effect on what grows back. Either alone is thin. Together they are a coherent
compound-disturbance paper, and B alone would be a re-analysis of a published model, which is a weak
shape on its own.

## 4. What is already computed, and verified

Run against the rasters on 2 August 2026. **These numbers are trustworthy but the code was ad hoc;
under the house rule nothing may be quoted in a manuscript until the code is checked into the
pipeline.** Reproduce them before use.

The four intersection rasters in `3.SpatialData/beetle_fire_interactive/` were decoded. They are on a
136 x 67 grid at 29.6 m over the roughly 8 km2 fire clip, and their coding is:

- `0` = neither agent
- `1` = one agent only
- `2` = **both agents**, which is the co-occurrence class

`mpbred_firehigh.tif` gives 67 co-occurrence cells; `mpbred_firelow.tif` gives 132. Cross-tabulating
against `Fire.High.NDBR.tif` and `Fire.Low.NDBR.tif` confirms every code-2 cell is burned, so the
decoding is right. Red-attack totals 493 cells in the clip, consistent from both rasters.

**The contingency table the published paper never reported:**

| Burn severity | Red-attack | Not attacked | Per cent attacked |
|---|---:|---:|---:|
| unburned | 8 | 4,868 | 0.2 |
| low | 132 | 2,115 | 5.9 |
| moderate | 286 | 1,149 | 19.9 |
| high | 67 | 487 | 12.1 |

**The pattern is non-monotonic**, peaking at moderate severity and falling at high. That is
interesting and it is exactly the kind of result that needs adversarial checking before it is
believed. See the traps in §6, particularly trap 1, which could manufacture this entire pattern.

## 5. Data inventory, with paths

Root: `/Users/seamus/repos/publications-pending/Darkwoods-Disturbance-Paper/`

| What | Path | State |
|---|---|---|
| Beetle by fire intersections | `3.SpatialData/beetle_fire_interactive/*.tif` | 4 rasters, decoded above, **never used in any manuscript or script** |
| Burn severity, classified | `3.SpatialData/fire_severity/Fire.{High,Med,Low}.NDBR.tif` | Binary masks per class |
| Beetle red stage | `3.SpatialData/beetle_stages/Beetle.Outbreak.RedStage.tif` | Binary |
| Beetle continuous surface | `3.SpatialData/beetle_stages/MPB.classified.spatstat.tif` | Continuous, the only surviving spectral surface |
| Beetle annual series | `3.SpatialData/beetle_stages/Beetle.Outbreak.{2005..2014}.tif` | 2008 and 2010 are **empty of code 44** |
| Grey stage | `3.SpatialData/beetle_stages/Beetle.Outbreak.GreyStage.tif` | Corrected union is 1,541 cells |
| Attack count | `3.SpatialData/beetle_stages/mpb_grey_attackcount.tif` | **STALE.** Built from the wrong 932-cell layer. Rebuild from the 1,541-cell union before use |
| Seedling point pattern | `3.SpatialData/seedlings/` | The response for question B, EPSG:32611 |
| Terrain and wind | `3.SpatialData/terrain_environment/` | Elevation, Slope, TWI, Rutm, Wind, Aspect, all 695 x 639 at 25 m |
| BEC zones | `3.SpatialData/bec_zones/BEC.ecozones.shp` | Three zones |
| Field plots | `3.SpatialData/plot_locations/` | 94 CBI fire plots, 28 beetle basal-area plots |
| Published model code | `4.RData/3.Seedlings/`, `4.RData/spatstat_refit_2026-06-01/` | The point-process refit lives here |
| Published manuscript text | `Archive/writing_outputs/20260613_053044_rs_methods_spinoff/sources/extract_FEM_FINAL_manuscript.md` | Table 9 and the model equation are at lines 845 to 882 |

## 6. Traps, in order of how much damage they would do

1. **The 0.2 per cent unburned figure is suspicious and may be an artefact.** If the beetle raster was
   clipped or masked to the fire perimeter at any stage, then "almost no beetle attack outside the
   burn" is a property of the clipping and not of the forest, and it would manufacture the entire
   association in §4. **Check the provenance and footprint of the beetle red-stage raster against the
   fire perimeter before believing any of it.** This is the single most important check in the whole
   scope, and if it fails, question A collapses to nothing.

2. **Direction of causation.** Beetle 2005 to 2014, fire 2015. Beetle precedes fire, so the arrow
   runs one way only. Do not write anything implying fire drove beetle attack.

3. **The shared-driver confound.** Both agents track host abundance and topography. Lodgepole-rich,
   mid-elevation stands are both more attackable and more burnable. Any association between them may
   be host distribution seen twice. The sibling beetle paper shows this exact effect: conditioning on
   lodgepole presence flattens most of an apparent terrain gradient. Get the host layer in early.

4. **Spatial autocorrelation.** Moran's I on the red-attack union is **0.728**. Naive p-values are
   worthless. The sibling paper uses a spatial block bootstrap at roughly 1 km blocks and reports
   effect sizes plus block intervals. Do the same. Do not report a raw p-value.

5. **Extent.** All of this sits inside the 8 km2 fire clip, which is where fire and beetle can
   co-occur at all. The sibling paper's central methodological finding is that **analysis extent can
   reverse the sign of a coefficient** in exactly this landscape. An 8 km2 study is precisely the
   extent it warns about. Handle this head on rather than hoping a referee misses it.

6. **Do not re-present the published index comparison.** Five fire indices and four beetle indices,
   their separability, ANOVA, SVM diagnostics and accuracy, are all in the FEM **main text** Tables 5
   to 8, its Supplementary S3 to S7, and three public GitHub repositories
   (`darkwoods_wildfire`, `darkwoods_beetles`, `darkwoods_seedlings`). Cite them, never re-table them.

7. **Grey-stage values.** Any reused beetle figure or number must use the corrected grey raster:
   1,541 cells, not the legacy 932. Corrected regeneration values are grey 33.6 per cent, 1,315
   seedlings; red 24.7 per cent, 965 seedlings.

8. **`dplyr::intersect` masks `terra::intersect`.** Namespace it. This broke a render in the sibling
   project.

## 7. Suggested sequence

**Phase 0, one session, cheap.** Resolve trap 1. Establish the true footprint of the beetle red-stage
raster relative to the fire perimeter and the wider landscape. If the beetle layer is confined to the
burn, stop and report; question A is dead and only question B survives. Everything downstream depends
on this.

**Phase 1.** Rebuild the contingency in saved, checked-in code. Bring in the host layer, either the
provincial inventory used by the sibling paper or the local BEC and species data, and recompute the
association conditioned on host. Report effect sizes with spatial block intervals, never naive
p-values.

**Phase 2.** Refit the published point-process model with the beetle by fire interaction term. Compare
against the published additive fit. Report honestly whether the interaction is supported, and note
that a significant result partially revises the parent paper, which is a normal and publishable
outcome if handled openly.

**Phase 3.** Decide the framing with the author before writing. If the interaction is null, the paper
is about compound-disturbance claims outrunning the models that support them, which is still a real
contribution. If it is significant, the paper is about the interaction itself.

**Phase 4.** Write as a single executable Quarto document, following the sibling paper exactly.

## 8. Optional, blocked, and out of scope

- **Cross-agent spectral separability** is blocked on re-acquiring Landsat and re-deriving the
  indices, per §2. Revisit only if the author wants to invest in reprocessing.
- **Temporal detection** across the annual series and **grain sensitivity** are both now claimed by
  the sibling beetle paper. Taking them here would create self-overlap.
- **Area-adjusted accuracy** on the published confusion matrices is an upgrade to published numbers,
  which is the weakest dual-publication shape. Use it as a section at most, never as the anchor.
- **Journal selection is the author's** and is untouched here. Note only that a **Forests
  feature-paper invitation dated 24 June 2026** exists and postdates every earlier venue scan.

## 9. House rules that apply

These come from the sibling project and are not optional.

1. **If it is not in the manuscript, it is not part of the study.** All analysis lives in live R
   chunks in the `.qmd`, every one carrying an explicit `#| echo: true`. No `echo: false`, no
   `include: false`, no `eval: false`. Data retrieval that genuinely cannot run inside a render may
   sit in a saved script, and the manuscript must say so and re-apply any screening decisions itself.
2. **Never report a number from code you did not save.** That includes every figure in §4 of this
   document.
3. **The master `.qmd` is the single source of truth.** Edit it, never a render.
4. **Verify the venue against the live guidelines**, not from memory.
5. **No em-dashes**, anywhere, including code comments and commit messages.
6. **Prefer text extraction over image rendering when reading PDFs.** Image reads of scanned journal
   PDFs are expensive and silently mangle numerals.

## 10. Repository to build, and its layout

Create the project at
`/Volumes/PortableSSD/Github/claude-science-library/publications-academic/beetle-fire-compound-disturbance/`,
as its own git repository with its own GitHub remote, then register it as a submodule of
`claude-science-library` the way the sibling papers are. Mirror the sibling's layout exactly; a
reader who knows one project should be able to navigate the other without being told anything.

```
beetle-fire-compound-disturbance/
├── 01.manuscript/          the .qmd and its renders. Edit the .qmd, never a render
│   └── archive/            superseded drafts, dated
├── 02.inputs/              one subfolder per dataset, each with its own README.md
│   ├── README.md           central provenance: every source, licence, retrieval date, traps
│   ├── beetle-fire/        the intersection rasters
│   ├── fire-severity/      classified burn severity
│   ├── beetle-stages/      red, grey, annual series, attack count
│   ├── seedlings/          the point pattern, the response for question B
│   ├── terrain/            elevation, slope, aspect, TWI, ruggedness, wind
│   └── archive/            superseded inputs, with a note saying what replaced what
├── 03.outputs/             figures and tables, plus build-readme.py
│   ├── PNG/                figures at 300 dpi minimum
│   ├── TBL/                tables as CSV
│   ├── MD/                 results notes
│   └── Archive/            superseded outputs, dated in the filename
├── 04.references/          bibliography and everything read
│   ├── references-compound.bib
│   ├── references-compound-manifest.md    provenance for every entry, see below
│   ├── literature/         the PDFs actually read, foldered by theme
│   ├── grandfather-study/  the published parent paper
│   ├── apa.csl and the venue CSL
│   └── archive/
├── 05.tasks/               task requests, progress log, scoping memos
│   ├── TASK-REQUEST-<date>.md
│   ├── progress.md         the running log; every phase, every correction, every trap found
│   ├── drafts/  figures/  references/  scripts/  sources/
│   └── archive/            superseded task requests, never deleted
├── _extensions/            vendored Quarto journal template
├── _quarto.yml
├── INDEX.md                the map: entry point, findings, layout, traps, open items
├── README.md               GENERATED from the render, never hand-edited
├── .gitignore
├── .gitattributes          Git LFS rules if bulk data is committed
└── beetle-fire-compound-disturbance.Rproj
```

Rules that go with the layout, all learned the hard way in the sibling project:

1. **Every `02.inputs/` subfolder carries its own `README.md`** giving source, publisher, portal
   URL, licence, retrieval date, local path, how the manuscript uses it, and its specific traps.
   `02.inputs/README.md` holds the central provenance table and must not contradict them.
2. **`04.references/compound-manifest.md` records where every bibliography entry came from**, which
   fields could not be extracted, and any disagreement between a filename and the PDF text. In the
   sibling project this caught two entries that were wrong rather than merely incomplete.
3. **`README.md` at the root is generated, not written.** Copy
   `03.outputs/build-readme.py` from the sibling. It reads the rendered HTML and emits the title,
   subtitle and abstract from the `.qmd` front matter, then every figure and table interleaved in
   manuscript order, as GitHub-flavoured pipe tables. GitHub does not render the Pandoc grid tables
   Quarto produces, so a paste of the render prints a wall of plus signs. Rerun it after every
   render.
4. **Copyrighted PDFs and bulk data.** If the repository is public, `04.references/literature/`
   contains other publishers' work and putting it there is a decision the author must make
   explicitly, not a default. If bulk data is carried, use Git LFS, and note that broad
   `02.inputs/**` LFS patterns will swallow `.md` and `.R` files as binary pointers unless the
   override uses `!filter !diff !merge`, since `text` alone does not undo `filter=lfs`.
5. **`INDEX.md` is the map a future session reads first.** Findings, layout, traps, open items. In
   the sibling project it is gitignored, so decide deliberately whether you want that here.
6. **Nothing is deleted, it is archived** with a dated filename and a line in `progress.md` saying
   what superseded it.

## 11. Environment

- R is the CRAN build at `/usr/local/bin/R`, currently 4.4.1, global library at
  `~/Library/R/arm64/4.4/library`. `terra`, `dplyr`, `ggplot2`, `knitr`, `kableExtra`, `patchwork`,
  `MASS` are installed. `spatstat` is needed for the point-process refit; check before assuming.
- Python is MacPorts `python3`, 3.12.
- Package management is MacPorts, never Homebrew.
- Data lives at `/Users/seamus/repos/publications-pending/Darkwoods-Disturbance-Paper/3.SpatialData/`.
  Set `DARKWOODS_DATA` to override.
- The sibling manuscript, worth reading as the pattern to follow, is at
  `/Volumes/PortableSSD/Github/claude-science-library/publications-academic/beetle-topography-and-wind-study/01.manuscript/beetle-topography-wind-study.qmd`.
  Its `INDEX.md` and `05.tasks/progress.md` carry the traps and conventions in full.
