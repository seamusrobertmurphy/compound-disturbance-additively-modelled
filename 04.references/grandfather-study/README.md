# The parent paper

Murphy, S., Leslie, A., Wilson, J., & Banks, L. K. (2026). Spatial patterns of conifer regeneration
following Mountain pine beetle outbreak (*Dendroctonus ponderosae*) and mixed-severity wildfire: A
point process model of disturbance interactions in the southern Selkirk Mountains, British Columbia.
*Forest Ecology and Management*, 618, 123985. https://doi.org/10.1016/j.foreco.2026.123985

Cited throughout as `murphy2026`. This study tests the interaction that paper's framing asserts and
its model does not fit.

## The PDF is not in version control

The file is the published version of record, marked "© 2026 Elsevier B.V. All rights reserved", and
this repository is public. It is gitignored and kept locally at
`04.references/grandfather-study/murphy-et-al-2026-FEM.pdf`. Retrieve it from the DOI above, or from
the author's own copy.

**This is the author's decision to revisit, not a settled one.** Elsevier's sharing policy permits
an author to post the accepted manuscript, as distinct from the version of record, in a
non-commercial repository after any embargo. If the accepted manuscript is wanted here, that is the
version to add, and the same question applies to anything placed in `../literature/`.

## What this study takes from it

| | |
|---|---|
| Model form | `Y_i = exp(b1 SSdist + b2 RA + b3 GA + b4 + BS + b5 RIX + b6 AS + b7 W + e_i)`, red attack, grey attack and burn severity as additive main effects with no product term |
| Response | 3,886 mapped seedlings across three 4 ha plots, seven conifer species |
| Beetle surfaces | Landsat NDMI red-attack classification; grey stage as the union of annual classifications 2005 to 2011 |
| Fire surface | Landsat dNBR burn severity, validated against field reference plots |
| Disturbance interval | Fire followed beetle by 1 to 11 years, median 7 |

The paper's own result on overlap is that areas of combined beetle mortality and high burn severity
carried significantly reduced lodgepole pine regeneration, while other conifers responded mainly to
fire severity and seed-source proximity. That result was obtained without an interaction term, which
is what makes the refit in Phase 2 a test rather than a repetition.
