# Frozen bootstrap baseline — 26 September 2026

This is the historical import baseline, not a live progress report. Current state is generated separately.

| Baseline object | Imported count / state |
|---|---|
| Source registry rows | 70 |
| Distinct registered identifier groups | 68; W45/W19 and W41/W11 share identifiers |
| Completed paper extractions in the source spreadsheet | 0 |
| Theory-family intake cards | 37; substantive review OPEN |
| Research workstreams | 86 (31 biological, 26 mathematical, 21 measurement, 8 validation) |
| Research gaps | 91 |
| Critical freeze blockers | 43; all OPEN |
| Tissue adapters | 6; all OPEN |
| MVCL mechanism vocabulary | 13 modules, overlays separate, 17 registered edges |
| Cancer model instances / empirical runs | 0 / 0 |
| Scientific decision | GO research; NO-GO mathematical kernel freeze |

## Source fidelity

The eight spreadsheet tabs are preserved as JSON and CSV. Source papers in the
registry are reading leads; earlier prose called them “verified”, but this bootstrap
has no per-paper verification receipts and does not promote that label. Duplicate
identifiers remain visible as aliases, not independent supporting studies.

Full user-authored source transcriptions are included under `sources/`. The two
MVCL masters are DOCX-to-Markdown conversions; project PDFs preserve page-labelled
text; native OoL kernel Markdown is retained exactly. FFBBP and MCM-HMWH are complete
indexed-text window assemblies with explicitly unavailable original PDF hashes.
No publisher full-text paper PDFs or patient datasets are redistributed.

## Known source discrepancies retained

The foundation master map still contains its earlier 33-anchor paragraph and an
incomplete arithmetic description of later additions. Its original export is kept
unchanged. Loop-of-Loops contains historical Seed–Sink–Switch–Spread wording;
MVCL v1.3's canonical order remains Seed–Switch–Sink–Spread. The earlier Permansson
EGR/Allfather integration spec is not substituted for the v0.1.6 generalized-regime
paper. None of these differences is silently reconciled in a frozen source.

## Import upgrades are not automatic

OoC v0.1.1 named older OoL/FFBBP versions. The provided OoL kernel is 2.7.7;
the available FFBBP source is 1.6.0. They are pinned reference material, not
newly qualified cancer implementations. Source-copy completion is not science completion.
