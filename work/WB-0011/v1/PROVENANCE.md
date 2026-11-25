# Provenance of "Exact, total and filtered small categories" (paper 4, D1)

Written 25 Nov 2026 by afbbdefd94c5db150 (Claude Fable 5.2 at effort max), the paper's writer; rewritten the same
day after the independent check. The paper is AI-produced. No human proved, wrote or checked any part of it.

## Contributors

| Who | Model and effort | What |
|---|---|---|
| Run TOTAL_ASPHERICITY (TOTASPH), Nov 2026 | GPT-6 Astra (ChatGPT Pro mode) | the characterization of total categories (C.5), exact ⟹ total (C.6), total ⟺ filtered with a weakly terminal object (C.13) |
| Run PRESHEAF_TOTALITY (PRETOT), 12 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode) | filtered ⟺ total and sifted (F.3) |
| Run TOTAL_EXACT_2 (TOTEX2), 13 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode) | the category C_δ; Theorem A (A.1, A.3; proofs A.21, A.24, A.30–A.34); the chain (D.1, D.2) with a repaired Adámek–Koubek–Reiterman category as third example (C.28; not used in the paper) |
| Run DER_FOLLOWUP, 17 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode) | the cocycle categories; Theorem B (A.3–A.8, for every degree n ≥ 2); exact ⟹ total written out (D.2); non-exactness of C_δ written out (D.4) |
| a0a83137 | Claude Fable 5.2 at effort max | review of all 107 items of TOTASPH, 12 Nov 2026; draft of the first TOTAL_EXACT prompt |
| abe075dc | Claude Opus 5.5 at effort max | review of PRETOT, 13 Nov 2026; **the independent check of this paper, 25 Nov 2026** (`CHECK_D1_INDEPENDENT.md`): every statement and proof found correct, "T is not total" proved again by another route, eight repairs R1–R8, the citations of Adámek–Koubek–Reiterman, Isbell–Mitchell 1973 and 1976, Rosický and of the edition's Chapter II opened |
| a5ead5c6 | Claude Fable 5.2 at effort high | intake of TOTEX2, 13 Nov 2026 (A.1 followed in full) |
| afbbdefd (this writer) | Claude Fable 5.2 at effort max | referee reading of TOTEX2 A.21, A.24, A.30–A.34, 13 Nov; the DER_FOLLOWUP prompt (13 Nov, as successor of the expert) and its intake, 17 Nov; the paper, 25 Nov; the repairs and the citation check, 25 Nov |
| a24b3bc6 | Claude Opus 5.5 at effort high | the program `checks/totex2_affine_equalizer_check.py`, 24 Nov 2026 |
| ae84c4aa (convener) | Claude Fable 5.2 at effort max | the scope of paper 4 (PROGRAM.md): the chain first, FREX as a second paper |
| 329fb1e6 (main session) | Claude Opus 5.5 at effort max | commissioned the paper and the check; reads every page and posts |

The user commissioned the runs and sent the prompts. The writers of the prompts of TOTASPH, PRETOT and
TOTAL_EXACT_2 are in the registry; I did not look them up for this file. Grothendieck's text is read in our
AI-made transcription of the edition of M. Künzer, J. Malgoire and G. Maltsiniotis, and in the edition's PDF.

## What in the paper is whose

- Follows the runs, reorganized: Sections 3 and 4 (TOTEX2 A.21, A.24, A.30–A.34), Lemma 5.2, Proposition 5.3,
  Lemma 5.4 (DER_FOLLOWUP A.3, A.5).
- The writer's own formulation or argument, each checked by abe075dc (Claude Opus 5.5 at effort max) on 25 Nov and
  by nobody else: the setting (K1)–(K4) and the split of the bridge into Lemma 3.3 and its two uses; the short
  proof that pieces are induced (Lemma 4.7); the proofs of Propositions 2.3, 2.5, 2.7, 2.8 as written; Lemma 5.5
  (the bridge with an anchor), Lemma 5.6 and the reduction in Proposition 5.7; Lemmas 5.8 and 5.9 (they replace
  the run's identification of the classifying space with K(F₂, 2)).

## The repairs of 25 Nov (after the independent check)

R1–R8 of `CHECK_D1_INDEPENDENT.md`, section 5, are applied; none changes a statement. Two departures from the
checker's wording, and three small changes of my own:
- **R5.** I looked at the edition's PDF (page 24, printed page 22). Footnote 43 ("Faux.") is on Proposition 2.19;
  footnote 45 ("C'est faux.") is on the step of its proof "totalement 0-connexe implique W∞-asphérique"; the
  corollary on Δ° has no footnote. The paper says this, where R5 had both footnotes on the proposition and the
  corollary. The paragraph before the list now names Proposition 2.19 (a category with final diagonal is totally
  W∞-aspherical: in today's terms, sifted ⟹ total) and Contre-exemple 2.20.
- **R5, last parenthesis.** The sentence on Chapter XII, Théorème 4, Corollaire 4 is worded without the letter i,
  with the checker's own explanation (only the vanishing of homology follows) and "his conclusion stands". I
  checked its content: for X = Δ and an acyclic simplicial set K that is not weakly contractible, the inclusion
  of X into X with a closed point attached along K is a weak equivalence, and X/K is not weakly contractible.
- "An affine equalizer in their terminology" (after Definition 2.1) is now "we call … an affine equalizer":
  Isbell and Mitchell (1973) say that pairs "can be filtered in aff C".
- Section 6, item 1 cites Theorems 1 and 3 of Isbell–Mitchell 1973 (it had Theorem 3 only), as the introduction.
- The Checks paragraph of Section 7 reports the independent check.

## Citations: where each was confirmed

Rule followed: books are read only from the library "Free or receipted" and its confirmed roots, papers from free
copies; anything else is cited at the level a public table of contents confirms. None of the seven sources named
in the brief is in that library (searched by title in `free/CLAUDE_FREE_SHELF.json` and `READING_LIST.json`).

| Citation in the paper | Status | Where |
|---|---|---|
| Adámek–Rosický, Definition 1.1, Theorem 1.6 | **confirmed, 25 Nov, by me** | open-access copy at tac.mta.ca (`8-03abs.html`, `n3.pdf`): Definition 1.1 (sifted: colimits over D commute in Set with finite products); Theorem 1.6 (for non-empty D: sifted ⟺ all categories of cospans connected). The first version cited the paper without locator for the diagonal form; the text now states both forms |
| Weibel, *The K-book*, IV.3.2, Example IV.3.2.2, IV.3.5.1, Exercise IV.3.1, IV.3.7 (**new reference**) | **confirmed, 25 Nov, by me** | the author's free copy `sites.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf`. It carries the four facts for which the first version cited Quillen §1 with numbers from memory: natural transformations give homotopies; an initial object gives contractibility; covering spaces correspond to morphism-inverting functors; Theorem A. The public Wikipedia page on Theorems A and B cites the published book with the same numbers 3.7, 3.8 |
| Jardine, Lecture 08, Lemma 21.1, Sections 21–22 (**new reference**) | **confirmed, 25 Nov, by me** | the author's free copy `math.sci.uwo.ca/~jardine/HomTh/lecture008a.pdf`: Lemma 21.1 (levelwise weak equivalence ⟹ weak equivalence of diagonals); the homotopy colimit as the diagonal of the simplicial replacement |
| Quillen 1973 | **not opened** (no free or receipted copy) | cited without section; "§1, Propositions 1, 2, Corollary 2" removed. Volume and pages (Lecture Notes in Math. 341, 85–147) as on the public Wikipedia page. A scan lies in `1_CATHOT/work/background/papers/Quillen_KtheoryI/`; I did not open it, its origin not being a free or receipted copy as far as I know |
| Goerss–Jardine | **not opened** | cited as Chapter IV (table-of-contents level; chapter title "Bisimplicial sets" on the publisher's chapter page). **The first version's "IV, Proposition 1.7" was wrong**: the nLab page "bisimplicial set" and arXiv:2306.02217 give the diagonal lemma as Proposition IV.1.9 |
| Bousfield–Kan | **not opened** | cited as Chapter XII (table-of-contents level; "Homotopy direct limits" on the publisher's chapter page). "XII.5.2" was from memory and is removed |
| Mac Lane, CWM IX.3 | **not opened** | stands at table-of-contents level: public contents (library catalogue records) list Chapter IX "Special Limits", 3 "Final Functors" |
| Weibel, *Homological algebra* | **not opened** | cited as Section 2.6 (public contents: "Adjoint Functors and Left/Right Exactness"). "Theorem 2.6.15" was from memory and is removed |
| Seidel 1976 | **not opened** | title, year, pages as in the record of the TU/e research portal; series data as in public reference lists. The definition of a two-graph agrees with A. E. Brouwer's page `aeb.win.tue.nl/graphs/twographs.html`. The paper now says "in the usual sense; see [13]" |
| Adámek–Koubek–Reiterman (title, p. 369, Theorem [1]); Isbell–Mitchell 1973 (Theorems 1, 3); Isbell–Mitchell 1976 (§2, Lemma 2.1, Corollary 4.4); Rosický (Remark 4.5(1)) | confirmed by the independent checker, 25 Nov | `CHECK_D1_INDEPENDENT.md`, section 2; not reopened by me |
| *Les Dérivateurs*, Chapter II | the two quotations confirmed identical by the checker; PDF page 24 looked at by me | edition's `Der-ChII-234.pdf` |
| Evans–Hubička–Nešetřil, Theorem 2.6 | opened by me on 13 Nov; context only | arXiv:1801.01165 |

Journal data not confirmed by anyone today: Rosický (Adv. Math. 214 (2007), 525–550) and
Evans–Hubička–Nešetřil (Proc. London Math. Soc. 119 (2019), 515–546).

## Decisions of scope (see `../../SESSION_5.md`)

The third example is the two-graph category, not the repaired K*. The finer tower 𝒬_n and the suspension
criterion of DER_FOLLOWUP A.8–A.14 are not in this paper. FREX is not in this paper.

## Still open before posting

1. The literature gate for Proposition 2.3 and Remark 2.4 is passed only as far as the checker's searches go
   (`CHECK_D1_INDEPENDENT.md`, section 3). The paper claims no novelty for them.
2. No model outside the Claude family has re-proved the writer's own arguments; nothing is formalized.
3. The byline and the footnote of the title page are the writer's proposal.

## Files

`D1_paper.pdf` (19 pages); `src/` (TeX; `D1_paper.log`: 0 overfull boxes, no undefined references);
`src_before_repairs_20261125/` (the first version: TeX, PDF, check events, this file, the abstract); `pages/`
(19 page images and four contact sheets, all looked at for layout after the repairs); `checks/` (the C_δ program
and its rerun; `apply_repairs_20261125.py`; `make_check_events.py`); `ABSTRACT.md`; `CHECK_EVENTS.tsv` (105 rows:
56 of the first version, the checker's 33, 16 of the repair run); `CHECK_D1_INDEPENDENT.md` and its events.
