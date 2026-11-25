# Provenance of "Exactness of colimits and amenability are independent for categories of finite substructures" (FREX)

Written 25 Nov 2026 by a848636d0bbf3ae4b (Claude Fable 5.2 at effort max), the writer of the paper and the agent of its
literature gate (`CONFERENCE/GATES_D2_FREX.md`, section 2). Brief: `agent_notes/FREX_PAPER_BRIEF_20261125.md`, from the
main session 329fb1e6 (Claude Opus 5.5 at effort max). The paper is AI-produced. No human proved, wrote or checked any
part of it. Not posted.

Checked on 25 Nov 2026 by ac59b1f5753a32bf7 (Claude Fable 5.2 at effort max): `CHECK_FREX_INDEPENDENT.md` with
`CHECK_FREX_INDEPENDENT_CHECK_EVENTS.tsv` (no theorem wrong; repairs R1-R7). The repairs are applied; see the section
"After the independent check" below. The text before the repairs is in `src_before_repairs_20261125/`.

Numbering of the paper: Definition 1.1; Theorems 1.2 (dictionary and topos), 1.3 (transfer), 1.4 (posets), 1.5 (vector
spaces); Corollary 1.6 (Evans's separation); Remark 2.1, Lemma 2.2, Definition 2.3, Proposition 2.4 (affine criterion);
Definition 3.1, Lemma 3.2 (Ramsey), Remark 3.3, Lemma 3.4 ((Re) gives amenability), Definition 3.5, Remark 3.6;
Lemma 4.1 (weights), Remarks 4.2, 4.3; Lemma 5.1.

## Contributors

| Who | Model and effort | What |
|---|---|---|
| Run FREX, final 18 Nov 2026 (`derivateurs_companion_20261109/pro_prompts_max_20261112_work/FRAISSE_EXACT/FREX_final_20261118T1235Z_unzipped/FREX/`) | GPT-6 Astra (ChatGPT Pro mode) | The results: `sections/A.tex`, statements `A:coinvariants` (first sentence of Thm 1.2), `A:convex` (the direction used in Lemma 3.4), `A:signed-averaging` (Thm 1.3, in the form of a closed co-precompact subgroup), `A:poset-weights` (Lemma 4.1), `A:ordered-posets` (Thm 1.4), `A:ordered-vector-amenability` (Thm 1.5 (a)), `notes/ordered_vector_obstruction.tex` (Thm 1.5 (c) over F_2 and Z, its lines 7-9 and 93-94), `notes/ordered_vector_rational_exactness.tex` (Lemma 5.1 and Thm 1.5 (b)) |
| An earlier run that FREX calls T (its item A.6) | GPT-6 Astra (ChatGPT Pro mode) | The first half of Lemma 3.2 (Ramsey property gives integral affine equalizers); known to the writer only through one sentence of FREX (`A.tex` l.195-199) |
| Intake of FREX, 19 and 24 Nov 2026 | Claude Opus 5.5 at effort max | followed every step of the run (`INTAKE_PILE_20261124/INDEX.md` l.387; `INTAKE_FREX_20261124_CHECK_EVENTS.tsv`) |
| a34c04448e8299803, connection map of 24 Nov (`MAP_HOMOTOPY_CATEGORIES.md`, K3) | Claude Opus 5.5 at effort max | the reading of exactness as a property of the topos, stated without proof |
| ac59b1f5753a32bf7, independent check of 25 Nov 2026 | Claude Fable 5.2 at effort max | every proof followed; Theorems 1.2, 1.3, Proposition 2.4, Theorem 1.5 (c) and the non-amenability of Theorem 1.4 proved again before reading; every citation but Hodges opened; both programs run; the repairs R1-R7, among them the converse in Remark 4.3, the last step of Theorem 1.3 (c) and the example of finite sets and injections in the introduction |
| a848636d0bbf3ae4b (this writer), 25 Nov 2026 | Claude Fable 5.2 at effort max | the literature gate; every proof derived again; the text; the program `checks/frex_checks.py`; and the items listed next |

## What the writer changed or added (25 Nov 2026; read by nobody else)

1. The setting of D1 (hexagon:2611.01026, section 3.1): a triple (M, G, K) with (K1), in place of the run's "setting (S)".
2. Proposition 2.4, both directions, proved directly from Theorem 1.2 by coinvariants. The run cites Isbell and
   Mitchell (1976) for it; the writer did not open that paper.
3. Theorem 1.3 stated with the finite sets E(B) = G_B\G/H and Definition 3.5, without completions or uniformities; part
   (c) through the inverse limit of the E(B).
4. The second sentence of Theorem 1.2 (the left adjoint of the constant functor on R-module objects of the topos of
   continuous G-sets) and Remark 2.1.
5. Lemma 2.2, Corollary 1.6 and Remark 4.3 (the bearing on Evans's Remarks 2.12).
6. Remark 4.2: the weights as values of Harman and Snowden's Euler-characteristic measure for Aut(R, <), and the
   three-point example showing that they are not multiplicative.
7. Remark 3.6: Theorem 1.3 in Zucker's notation.
8. Lemma 3.2: proof written out from the run's one-sentence description; its second half ((Re) from the Ramsey
   property by the minimax theorem) follows the run's `A:convex`.
9. Lemma 5.1: the passage from the theorem of Hubička and Nešetřil to the category C is the run's; the realization of
   C as a Fraïssé class in a relational language, so that Proposition 2.4 applies, is the writer's.

Not in the paper, although in the run: the run's own proof of non-amenability for ordered posets (the paper cites
Kechris-Sokić); the structural hypotheses (St), (Op), (Fin) and totality of the two examples; the cocycle classes
A_r(Λ); the comparison table; the statement that amenability with metrizable universal minimal flow gives rational
exactness; Part C (the run's C.10-C.13 concern another question and were not read).

## Citations

- Opened by the writer on 25 Nov 2026, at the places cited (copies in `agent_notes/GATES_D2_FREX_sources/`):
  Harman-Snowden arXiv:2204.04526v2 (Def. 3.1, Ex. 3.5, Prop. 4.8, Rem. 10.10, Thm 16.7, Rem. 16.8; journal data from
  Crossref); Snowden arXiv:2609.02021v1 (Prop. 8.2); Evans arXiv:2603.29606v2 (Thm 1.4, Cor. 1.5, Rem. 2.12, Lemma 3.7);
  Caramello arXiv:0805.2778v3 (Thm 2.9, Prop. 2.10; numbering reconstructed from the TeX); Di-Li-Liang-Xu
  arXiv:2108.13600v4 (Thm 5.1 and the equivalence after it); Kechris-Sokić 2012 (Remark 3.2, pp. 78-79); Zucker 2014
  (section 3, Thm 3.1, p. 45); D1 (section 3.1 of its source).
- Opened by the run FREX and by the independent check (ac59b1f5753a32bf7, Claude Fable 5.2 at effort max), at the
  places cited, not by the writer: Bodirsky 2014, Cor. 1.4 (3) (arXiv and journal versions); Hubička-Nešetřil
  arXiv:1606.07979v4, Thm 4.46; Isbell-Mitchell 1976, Thm 3.1, Prop. 3.3 and the remark after it;
  Kechris-Pestov-Todorcevic 2005, Thm 4.8 (for Fraïssé order classes) and Thm 2.2.
- Opened by the independent check only: von Neumann 1928, p. 305 (the minimax theorem, for two simplices).
- Not opened by anyone: Hodges, Model theory, section 7.1; the theorem used is Kechris-Pestov-Todorcevic, Thm 2.2.
  Mac Lane-Moerdijk's book: Artin's theorem is quoted from Di-Li-Liang-Xu, Thm 5.1.

## What is unconfirmed

- The repaired text (after R1-R7) has been read by its writer only; the main session reads every page before posting.
- The paragraph added to the introduction departs in one clause from the checker's wording (see below); that clause
  and the example of the translations of Z have not been seen by the checker.
- The search of the literature covers titles and abstracts, not full texts (`CONFERENCE/GATES_D2_FREX.md`, 2.3).

## After the independent check (25 Nov 2026)

Repairs applied to `src/FREX_paper.tex` with the wording of `CHECK_FREX_INDEPENDENT.md` (pages of the rebuilt PDF):
- R1, Remark 4.3 (p. 10): "The converse fails" was false for Corollary 1.6 as stated; replaced by the proof that the
  membership test with U = G implies exactness, and by the remark that only the weaker property of Evans's
  Remarks 2.12 is trivial for finite groups.
- R2, proof of Theorem 1.3 (c) (p. 8): the passage from k-algebras to Q-algebras by a Q-linear retraction.
- R3, Remark 3.3 (p. 6): Kechris-Pestov-Todorcevic, Theorem 4.8, quoted for Fraïssé order classes.
- R4, R5, introduction (p. 3): "over a field of characteristic 2"; the example of finite sets and injections (amenable,
  exact exactly over Q-algebras); what is left open.
- R6 (a)-(l) (pp. 1, 2, 3, 4, 5, 6, 9, 10, 14), (m) (`checks/frex_checks.py`, docstring), (n) (`CHECK_EVENTS.tsv`,
  type "original proof (not a check)" for the rows of original proofs); R7, the paragraph "Checks" (p. 14).
- One departure from the report's wording, in R5. The report's last sentence says that we do not know "whether
  amenability implies exactness over Q in general". That is not open: for M = Z with the group of translations and
  all finite subsets the group is discrete and amenable, and the two arrows {0} -> {0,1} have no affine equalizer over
  any non-zero ring (the run has this example, `sections/A.tex`, `A:translation`, and a second one,
  `A:cocycle-amenability`, amenable and not exact over Q, which was not checked for this paper). The paragraph says
  this instead and keeps the open question on rings in which 2 is invertible and which are not Q-algebras.
- The checker's events are merged into `CHECK_EVENTS.tsv` (63 rows).

## What the independent check was asked to cover (done; see `CHECK_FREX_INDEPENDENT.md`)

1. Theorem 1.2: the identification colim = S(V)_G and the functor T; the statement about the topos.
2. Proposition 2.4, both directions (the new proofs).
3. Lemma 3.2 (the character with value at distance at least 1/3; the minimax step) and Lemma 3.4.
4. Theorem 1.3 (a), (b), (c), in particular that s_N is well defined, invariant and natural.
5. Lemma 4.1 (the count m(-1)^b + (m+1)(-1)^(b+1)) and the identification of E(B) with the linear extensions in the
   proof of Theorem 1.4; the two citations it rests on (Bodirsky; Kechris-Sokić).
6. Theorem 1.5 (a): the variance bound and the choice of n; (c): identities (1), (2) and the five arrows; (b): Lemma 5.1
   (against the text of Hubička-Nešetřil), Step 2 (the bijection between E_i and E_i', identity (3)) and Step 3.
7. Corollary 1.6 and Remark 4.3, including the sentence that the converse fails.
The program `checks/frex_checks.py` (output: ALL CHECKS PASSED) covers Lemma 4.1 up to five points, the example of
Remark 4.2 and the two identities of Theorem 1.5 (c) for targets of dimension 3, 4, 5.

## Before posting: the main session (329fb1e6, Claude Opus 5.5 at effort max), 25 Nov 2026 ~06:00-06:15 UTC

- Read every page of the repaired build (pp. 1-7 before, pp. 8-15 after the session's compaction), the translation
  example of the introduction checked within (K1), and the checker's own non-amenability proof
  (`CHECK_FREX_INDEPENDENT.md`, section 3.1) followed to the end.
- Credit corrected: the run states Theorem 1.5 (c) over F_2 and Z only (`notes/ordered_vector_obstruction.tex`, lines
  7-9 and 93-94); the extension to every ring in which 2 is not invertible, by reduction to R/2R, is the writer's.
  "What is whose" now says so (`src/FREX_paper.tex`, the paragraph and the writer's list); backup of the source before
  this edit: `src/FREX_paper_before_main_credit_fix_20261125.tex`. Rebuilt: 15 pages, 0 overfull, 0 underfull, no
  undefined references; pages 13-15 read again.
- Deposit: `build_deposit_frex.py` (upload copy `upload/exactness_colimits_amenability.tex`, identical to the source up
  to line endings; `HEXAGON_METADATA_FREX.json`); state `HEXAGON_STATE_FREX.json`.

## Build

`src/FREX_paper.tex`, pdflatex (MiKTeX), three passes, 25 Nov 2026, after the repairs: 15 pages, 0 overfull boxes, 0
underfull boxes, no undefined references. All pages rendered at 60 dpi and looked at as contact sheets (`pages/sheet_1.png`,
`pages/sheet_2.png`); nothing runs off the page.
