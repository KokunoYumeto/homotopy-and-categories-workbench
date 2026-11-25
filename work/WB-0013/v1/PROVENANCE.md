# Provenance of "Classifying spaces of finite monoids with bounded homology" (paper 6, D2)

Written 25 Nov 2026 by afceadd46f7598ec4 (Claude Fable 5.2 at effort max), the paper's writer and the author of its
main theorems. The paper is AI-produced. No human proved, wrote or checked any part of it. Not posted.

Revised twice on 25 Nov 2026 by the same writer: after the literature gate, and after the independent check (the two
sections before "Build"). **The current state of the citations and of what is unconfirmed is in the section
"Revision after the independent check"**; the sections before it are kept as they were written, with a note where
they are out of date.

## Contributors

| Who | Model and effort | What |
|---|---|---|
| Run CATHOT, 10 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode) | statements G.4, G.6: a finite monoid whose classifying space is homotopy equivalent to a finite-dimensional complex has trivial universal group (the group eMe of the minimal ideal, the Karoubi envelope, Miller's Theorem B); Conjecture 7.1 of arXiv:2610.38760v1 fails, with RP² as counterexample; the three-object category of type RP² (G.11) |
| afceadd46f7598ec4 (this writer) | Claude Fable 5.2 at effort max | check of G.4, G.6 against the primary texts, 12 Nov 2026 (`G6_VERDICT.md`, `EMAIL_CLAIMS_CHECK.md`); **Theorems 2.1, 1.1, 1.2 and Corollaries 2.2, 3.3, 3.4, 1.4 of the paper**, 12 Nov 2026 (`OWN_RESULTS.md` sections 1-2, in `derivateurs_companion_20261109/pro_reviews_max_20261112/1_CATHOT/`); the prompts FINMON and S2COUNT (drafts of 12 Nov); the paper, the new form of the proof of Theorem 2.1, the program `checks/d2_examples_check.py`, 25 Nov 2026 |
| Earlier check of G.6, 11 Nov 2026 | Claude Fable 5.2 at effort medium | `pro_reviews_20261110/1_CATHOT/REVIEW_G6.md`: found G.4, G.6 correct; ruled void by the user because of the effort setting and redone on 12 Nov |
| A second reader (id not known to the writer; named in the brief of 25 Nov) | Claude Fable 5.2 at effort max | re-derived Theorems 1.1, 1.2 in the form of 12 Nov |
| A targeted check (id not known to the writer; named in the brief of 25 Nov) | Claude Opus 5.5 at effort high | targeted check of Theorems 1.1, 1.2 in the form of 12 Nov |
| Run S2COUNT, final 16 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode) | Proposition 5.2 (c) and the resolution used for (b): the monoids M_r, of which M_6 = M_1 (`sections/A_agent.tex`) |
| Run FINMON, 12-17 Nov 2026 (checkpoint 20) | GPT-6 Astra (ChatGPT Pro mode) | the monoid M_23, its resolution, the cocycle u, Proposition 5.3 (`sections/B_CP23.tex`, row B4-CP2); proofs of Theorems 1.1, 1.2 along the route suggested in its prompt (rows A:filtration, A:representation, A:bounded; not read by the writer); the observations of Remarks 2.3 (b) and 5.1 (its A3.4, A3(ii)); Proposition 5.2 (c) again (row E3) |
| The DERIVATEURS reader | Claude Opus 5.5 at effort high | intake of S2COUNT and FINMON at statement level, 17 Nov 2026 (`INTAKE_S2COUNT_REVLOC_20261117.md`, `INTAKE_DER_FOLLOWUP_FINMON_20261117.md`) |
| ae84c4aa (convener) | Claude Fable 5.2 at effort max | scope of paper 6 (PROGRAM.md, entry 6) |
| 329fb1e6 (main session) | Claude Opus 5.5 at effort max | commissioned the paper (brief of 25 Nov 2026); wrote to the author of arXiv:2610.38760 on 12 Nov 2026; opened Fiedorowicz 1984 (pp. 321-324) and McDuff 1979 (all eight pages) on 25 Nov 2026, in copies supplied by the user (`CONFERENCE/GATES_D2_FREX.md`, addenda 1 and 2) |
| a848636d0bbf3ae4b (literature gate) | Claude Fable 5.2 at effort max | the search of the literature, 25 Nov 2026 (`CONFERENCE/GATES_D2_FREX.md`, sections 1.1-1.4): four related results to cite; the stronger form of Corollary 3.4 through Gray-Pride's functor; the example Z/p² → Z/p of Remark 2.3 (a); the question of Remark 3.5 |
| abe075dcdd909eea0 (independent check) | Claude Opus 5.5 at effort max | the check of the whole paper, 25 Nov 2026 (`CHECK_D2_INDEPENDENT.md`, `CHECK_D2_INDEPENDENT_CHECK_EVENTS.tsv`): every proof read, both examples recomputed with its own program, the citations opened; ten repairs R1-R10; the observation at the end of Remark 3.5 (the map j_e is null-homotopic when the homology is bounded); the remark on the case a = g of Ben-Bassat's Example 3.4 |

The user commissioned the runs and the work. O. Ben-Bassat (arXiv:2610.38760v1) is the author of Theorem 1.3
(his Theorem C), of Conjecture 7.1, of the map j_e and Lemma 2.4 used in Lemma 3.2, and of the surjectivity of η
(his Section 7); he was informed of the counterexample on 12 Nov 2026 and answered (private correspondence, not
quoted in the paper). On 25 Nov 2026 the arXiv abstract page showed v1 as the only version. Z. Fiedorowicz (Amer. J.
Math. 106 (1984), p. 323) is the author of the monoid with five elements whose classifying space is equivalent to S²
(the monoid M_5 of Section 5) and of the suggestion that Ben-Bassat states as Conjecture 1.1 and proves as Theorem C.
D. McDuff (Topology 18 (1979), Lemma 1, p. 314) is the author of Lemma 3.1 (a).

## What the paper contains

Theorem 2.1 (maps BG → X, G finite, X with finite skeleta and bounded p-local cohomology: every finite-dimensional
representation of π₁(X) is trivial on the images of the p-elements), Corollary 2.2, Remark 2.3; Lemmas 3.1, 3.2;
Theorems 1.1, 1.2 with proofs; Corollaries 3.3, 3.4, 1.4, 1.5; Remarks 4.1, 5.1; Proposition 5.2 (six-element
monoid: U = 1, homology Z in every degree ≥ 2, classifying space a wedge of spheres) and Proposition 5.3 (23-element
monoid of type CP²), both with proofs; since the revision after the independent check, an unnumbered paragraph on
Fiedorowicz's monoid with five elements (a submonoid of the six-element monoid; type S², with proof); a provenance
section. The numbering of the statements has not changed since the revision after the gate.

## Citations: where each was confirmed

Opened by the writer (12 Nov 2026 unless said; freely accessible copies):
- Ben-Bassat, arXiv:2610.38760v1: the whole TeX source (Theorem C; Conjecture 7.1, source lines 1282-1285; the
  introduction's definition of j_e; Lemma 2.4; Section 7). Abstract page fetched again 25 Nov 2026: only v1.
- Miller 1984: pp. 39-41 and 84-85 (Theorem B = Theorem 10.1), page images of the copy on the author's page; the
  1985 correction.
- Atiyah 1961 (Numdam): (6.10)-(6.13), (7.1)-(7.9), (8.1), page images.
- Sweeney, arXiv:2502.05276v2: sections 1, 2 (Lemma 2.1, Proposition 2.2, Corollary 2.3) and 5 (Example 5.2).
- Palmer-Wu, arXiv:2510.16879v1: introduction (Theorem A, properties (1), (4), (5)).
- Carcacía-Campos, arXiv:2611.09718v1: statement of Theorem 6.2.
- Hatcher: statement of Proposition 4C.1.

**Locators that still needed opening at the first writing** (given from memory or from the citing papers; out of
date: all of them except Atiyah-Hirzebruch 1961 have since been opened by the gate's reader, by the checker or by the
main session, see the last two sections):
- Atiyah-Hirzebruch 1961, section 2, and Atiyah 1961, section 2: the multiplicative filtration and the spectral
  sequence, used as (K1), (K2). The exact numbers of the statements are not given in the paper.
- McDuff 1979, Lemma 1 (π₁(BM) = U(M)); Quillen 1973, section 1, Proposition 1 (π₁ of BC as the automorphism group in
  the groupoid completion).
- Hatcher: Example 2.43 (lens spaces), Proposition 1B.9 (maps into a K(G,1)), Corollary 4.33 (homology Whitehead
  theorem), section 4.B (Hopf invariant: homomorphism, value 1 on the Hopf map).
- Swan 1960 (title, pages and statement from memory and from Sweeney's citation).
- Fiedorowicz 1984, p. 323 (the conjecture; from Ben-Bassat's citation).
- The literature search for earlier occurrences of Theorems 1.1, 1.2 (Ben-Bassat, Martinian-Steinberg, Sweeney,
  Fiedorowicz 1984, McDuff, in full text) was taken out of this task by the main session and is being done by
  another agent. The writer's own search of arXiv on 12 Nov 2026 found no such statement (queries in
  `1_CATHOT/READING_BASE.md`, section 8). No query of the literature corpus was made for this paper.

## What is unconfirmed

(The first two points are the state at the first writing. Since then abe075dcdd909eea0, Claude Opus 5.5 at effort
max, has read the proof of Theorem 2.1 in the form of the paper and found it correct, and has confirmed (K1), (K2)
in Atiyah 1961, section 2; see "Revision after the independent check".)

- The proof of Theorem 2.1 in the form of the paper (finite skeleta, local at p, lens spaces) has been read by nobody
  but its writer. The checks by the second Claude Fable 5.2 at effort max and by Claude Opus 5.5 at effort high
  concern the form of 12 Nov (represented K-theory of BM, integral and p-local cases treated separately).
- (K1), (K2): quoted, locators unopened (see above).
- Theorem 1.3 is from an unrefereed preprint; the writer read its proof in full and found no gap.
- The run FINMON's statement that no monoid with fewer than 23 elements has type CP² is not checked and is not
  asserted in the paper.
- In `CHECK_EVENTS.tsv` the rows whose outcome begins with "the original" record where a statement was first proved;
  the fixed vocabulary of types has no word for that, and "independent re-proof" there does not mean a second proof.

## What the re-proof by another model family must cover

1. Theorem 2.1 as stated (hypotheses: X connected, finitely many cells in each dimension, H^q(X; Z_(p)) = 0 for
   q > n; conclusion for elements of p-power order), in particular Step 2 (the induction over the skeleta, which uses
   H^m(X^{m+1}; Z) = H^m(X; Z)) and Step 3 (K_1 of a lens space is a finite p-group; Atiyah's (8.1) and (6.11)).
2. Lemma 3.2: that B(eMe) → BM induces the surjection η|eMe on fundamental groups.
3. Theorem 1.1, including the passage from H_k(M; F_p) = 0 for large k to H^q(BM; Z_(p)) = 0 for large q, and
   Theorem 1.2 (iii) ⇒ (i).
4. Whether the hypothesis "finitely many cells in each dimension" in Theorem 2.1 can be dropped, and a search for a
   counterexample to Theorem 1.1 among small monoids with U(M) ≠ 1 (the run FINMON reports a census of order 7).
5. (Added after the two revisions.) Corollary 3.4 in its present form (a projective resolution of finite length of
   the trivial module forces eMe = 1); the paragraph "The monoid with five elements" of Section 5; and the
   construction in Remark 2.3 (b) of a classifying space with finitely many cells in each dimension for a group of
   type F_n for every n. The last two have been read only by the writer.
The examples are verified by the program `checks/d2_examples_check.py` (output `checks/d2_examples_check.out`:
ALL CHECKS PASSED), written independently of the runs' programs.

## Revision after the literature gate (25 Nov 2026)

The literature gate was written by a848636d (Claude Fable 5.2 at effort max):
`CONFERENCE/GATES_D2_FREX.md`, sections 1.1-1.4; its sources are in `agent_notes/GATES_D2_FREX_sources/`. Its
verdict: Theorems 1.1, 1.2, 2.1 and the failure of Conjecture 7.1 were not found in the literature; four related
results were uncited. The writer applied its eleven items (section 1.2) the same day:

| Item | Change in the paper | Page |
|---|---|---|
| 1 | new paragraph "What was known" in the introduction: Steinberg, Theorem A and Theorem 3.1; Martinian-Steinberg, Corollary 5.15 (also Theorem C, Corollary 5.16); Gray-Pride's restriction functor; the sentence presenting Corollary 3.4 as an application of Theorem 1.1 removed | 2 |
| 2 | "suggested by Fiedorowicz (p. 323, as quoted in Martinian-Steinberg, p. 1) and stated as a conjecture in Ben-Bassat" | 2 |
| 3 | Swan cited at Corollary 1 (and Corollary 2 for homology) | 2 |
| 4 | Lemma 3.1 (a): the proof from the presentation of the fundamental group of a nerve with one vertex added; McDuff cited as the original | 5 |
| 5 | Lemma 3.1 (c): said to be known; Sweeney, section 2.1 and Lemma 2.1 with his attributions, and Steinberg, p. 7 | 5 |
| 6 | Corollary 3.4 now concludes that the group H = eMe of the minimal ideal is trivial, with a proof by the functor A ↦ eA (Gray-Pride, Lemmas 2-4, Theorem 2) and Swan's Corollary 1; the freeness of the action of H on eM is proved directly by the writer, without Rees coordinates; Remark 3.5 keeps the two other routes to U(M) = 1 (Theorem 1.1; Gray-Steinberg, Theorem 6.27 and Corollary 6.7, with Miller) | 6 |
| 7 | after Corollary 3.3: Ben-Bassat's Example 3.4 (11 elements, universal group Z/2) and the comparison with Sweeney's Table 1 and Examples 5.4, 5.5 | 6 |
| 8 | Remark 3.5: the question whether bounded homology forces H = 1 | 6-7 |
| 9 | Remark 2.3 (a): the example Z/p² → Z/p, where the map on integral cohomology vanishes above degree 2 | 4 |
| 10 | bibliography: Gray-Pride, Gray-Steinberg, Martinian-Steinberg, Steinberg added (16 entries); Fiedorowicz 2002 (optional) not added | 12 |
| 11 | Section 6: who contributed the new form of Corollary 3.4, the sentence of item 9 and the question; Swan opened; McDuff 1979 and Fiedorowicz 1984 not opened; the search is in the records | 11 |

State of the citations after the gate. Opened by the gate's reader (not by the writer): Swan 1960 in full
(Theorem 1, Corollary 1 on p. 885, Theorem 2, Corollary 2 on p. 887); Steinberg, arXiv:2405.06594v1 (pp. 1-10);
Martinian-Steinberg, arXiv:2511.12657v1 (pp. 1-3, 12-14); Gray-Pride, arXiv:1003.3227v1 (pp. 4-6, section 8);
Gray-Steinberg, arXiv:1706.04387v1 (sections 6.3-6.4); Fiedorowicz 2002; Sweeney's Table 1 and Lemma 2.1 again.
**Still unopened by anyone on our side: McDuff 1979 (Lemma 1) and Fiedorowicz 1984 (pp. 322-324).** The paper
cites them through Ben-Bassat, Sweeney and Martinian-Steinberg, and Lemma 3.1 (a) now carries its own proof.
(Out of date: both were opened later the same day by the main session, and the locators "from the writer's memory"
named next were opened by the checker, except Atiyah-Hirzebruch; the journal pages are now in the bibliography. See
the next section.)
Still from the writer's memory: Atiyah-Hirzebruch 1961 section 2 and Atiyah 1961 section 2 for (K1), (K2); Quillen
1973 section 1 Proposition 1; Hatcher Example 2.43, Proposition 1B.9, Corollary 4.33, section 4.B.
The page range of Gray-Pride in the journal and the pages of Gray-Steinberg are not given in the bibliography.

Unconfirmed after the revision: the proof of Corollary 3.4 has been read only by the writer and by the reader who
proposed the derivation; the re-proof by another model family should cover it as well (the statement: a finite
monoid whose trivial module has a projective resolution of finite length has H = eMe = 1).

## Revision after the independent check (25 Nov 2026)

The check was made by abe075dcdd909eea0 (Claude Opus 5.5 at effort max): `CHECK_D2_INDEPENDENT.md`, with its own
rows in `CHECK_D2_INDEPENDENT_CHECK_EVENTS.tsv` (now merged into `CHECK_EVENTS.tsv`). Its verdict: no mathematical
error in any proof; both examples recomputed with its own program; one clause wrong as worded (Corollary 1.5, last
clause); ten repairs R1-R10. It is a Claude model: the check does not replace the re-proof by another model family.
In the same hours the main session 329fb1e6 (Claude Opus 5.5 at effort max) opened Fiedorowicz 1984 and McDuff 1979
in copies supplied by the user (`CONFERENCE/GATES_D2_FREX.md`, addenda 1 and 2; `PENDING_EDITS_20261125.md`). The
writer applied all of it the same day (pages of the build of 14 pages):

| Repair | Change in the paper | Page |
|---|---|---|
| R1 | Corollary 1.5, last clause: "every connected finite CW complex whose fundamental group is finite and non-trivial" (as first written the clause counted the circle, which does not satisfy the hypothesis of Conjecture 7.1) | 2 |
| in place of R2 | introduction: Fiedorowicz cited directly at p. 323, for his monoid with five elements of type S² and for his suggestion (paraphrased, not quoted); "Ben-Bassat stated this as Conjecture 1.1 and proved it"; the citation through Martinian-Steinberg removed | 2 |
| R3 | (K1), (K2): Atiyah 1961, section 2 named for the definition and the multiplicativity of the filtration, with (2.2) and Proposition (2.4) for its graded quotients (sentence reworded, same content) | 3 |
| R4 | lens spaces: the cohomology is read off from the cellular chain complex of Hatcher, Example 2.43 | 3 |
| R6 | Remark 2.3 (b): the group is "of type F_n for every n" (defined in the text); the passage to one classifying space with finitely many cells in each dimension is now proved in the remark (skeleton by skeleton, by Schanuel's lemma). The check asked for a reference and had none; the writer gives the argument instead of a locator from memory | 5 |
| McDuff | Lemma 3.1 (a): "McDuff, Lemma 1, p. 314" | 5 |
| R7 | after Corollary 3.3: "in the case a = 1 of that example"; added: the converse of Corollary 3.3 fails, by the case a = g of the same example (trivial universal group, classifying space the cofibre of RP¹ ⊂ RP^∞, reduced homology Z in degree 2 and Z/2 in every odd degree ≥ 3) and by M_6. The sentence proposed by the check gave only the groups Z/2; the writer computed the homology from the cellular chains and added the group Z in degree 2 | 6 |
| observation of the check, section 2.6 | Remark 3.5, three sentences at the end: when the homology is bounded the map j_e is null-homotopic (Miller, Theorem A, p. 39), so it cannot decide whether eMe = 1 | 7 |
| R9 | Remark 4.1: the three-object model of RP² is attributed to Tanaka in Carcacía-Campos | 7 |
| Fiedorowicz's monoid | Section 5.1: the elements 1 and x_ij of M_6 form Fiedorowicz's monoid M_5 (one sentence at the definition of M_6); new unnumbered paragraph "The monoid with five elements" after the proof of Proposition 5.2: a projective resolution of length 2, H_2 = Z, and BM_5 ≃ S² by the map s_2 (a proof of the exercise of Fiedorowicz, p. 323, from the proof of Proposition 5.2); adjoining y to M_5 changes S² into the wedge of the spheres of all dimensions ≥ 2 | 8, 9 |
| R5 | Proposition 5.3: Hatcher, Example 4.51 (π_3(S²)) and Proposition 4B.1 (the Hopf invariant is a homomorphism) | 11 |
| R10 | Section 6: Fiedorowicz and McDuff in "What is whose"; the check, its verdict, the same-family caveat and the two additions read only by the writer in "Checks"; who opened what in "Citations"; the records as a list (four files) | 11-13 |
| R8 | bibliography: Fiedorowicz "no. 2"; Gray-Pride "no. 12, 3005-3024"; Gray-Steinberg "no. 7, 3083-3170" | 13 |

R2 itself (keep the citation through Martinian-Steinberg, add Ben-Bassat's section 1 for the page) was not applied:
the direct citation takes its place, on the main session's instruction. The optional parts were applied (R4, R9, the
second half of R7, the observation for Remark 3.5).

**Fiedorowicz 1984 and McDuff 1979 were opened by the main session 329fb1e6 (Claude Opus 5.5 at effort max), not by
the writer: McDuff in full, Fiedorowicz at pp. 321-324 according to addendum 1 (the main session's instruction to
the writer says that it read both papers).** Fiedorowicz, Amer. J. Math. 106 (1984), no. 2, 301-350: pp. 321-324 read;
p. 323 holds the five-element monoid {1, x_ij}, x_ij x_kl = x_il, with BM equivalent to S² (an exercise there) and
the sentence that it seems likely that any finite simply connected complex is the classifying space of a finite
monoid; nothing there concerns bounded homology or universal groups of finite monoids. McDuff, Topology 18 (1979),
313-320: all eight pages read; Lemma 1 (p. 314) is as the paper uses it; every monoid constructed there is infinite.
**Neither states D2's theorems: Theorems 1.1, 1.2 and 2.1 are neither stated nor implied in McDuff's paper or on
these pages of Fiedorowicz's (the verdicts of the two addenda).**

State of the citations now. Opened by the checker at the places cited (its section 3): Atiyah 1961 (section 2,
(8.1), (6.11)); Ben-Bassat (TeX source: Theorem C, Conjectures 1.1 and 7.1, Example 3.4, section 7, Lemma 2.4, the
introduction, Theorem A); Carcacía-Campos, Theorem 6.2; Gray-Pride; Gray-Steinberg; Hatcher (Examples 2.43 and 4.51,
Propositions 1B.9, 4B.1 and 4C.1, Corollary 4.33); Martinian-Steinberg; Miller (Theorems A and B, Theorem 10.1);
Palmer-Wu; Quillen, section 1, Proposition 1; Steinberg; Swan; Sweeney. Opened by the main session: Fiedorowicz,
McDuff. Opened by the writer on 25 Nov 2026 for this revision: Ben-Bassat's Example 3.4 and Conjecture 1.1 (text of
v1). **The one locator still from memory: Atiyah-Hirzebruch 1961, section 2** (the paper gives Atiyah 1961, section
2 next to it, which the checker opened). No source is cited for the passage from "type F_n for every n" to a
classifying space with finite skeleta; the remark carries the argument.

Unconfirmed after this revision:
- the paragraph "The monoid with five elements" and the argument added to Remark 2.3 (b) were written after the check
  and have been read only by the writer. The first is confirmed by the writer's program `checks/d2_m5_check.py`
  (output `checks/d2_m5_check.out`: ALL CHECKS PASSED; it also computes H_1, H_2, H_3 of the bar complex of M_5
  without the resolution) and agrees with the writer's check of 12 Nov 2026 (`1_CATHOT/EMAIL_CLAIMS_CHECK.md`, claim
  (g), where the monoid is called P_2);
- the homology of the cofibre of RP¹ ⊂ RP^∞ (paragraph after Corollary 3.3) was computed by the writer; the checker
  computed the odd degrees;
- (done 25 Nov 2026) the main theorems were derived again by GPT-6 Astra (ChatGPT Pro mode) in FINMON_CP2, checkpoint 02
  (06:12 UTC), `converse/R9_section.tex`; posted as hexagon:2611.01042v1 (06:30:43 UTC; `POSTING.md`).

## Build

`src/D2_paper.tex`, pdflatex (MiKTeX), three passes. First build, 25 Nov 2026: 11 pages. Build after the gate,
25 Nov 2026: 12 pages, 0 overfull boxes, 0 underfull boxes, no warnings; all twelve pages looked at; pages changed
by that revision: 2, 4, 5, 6, 7 (top), 11, 12.

**Build after the independent check, 25 Nov 2026: 14 pages, 0 overfull boxes, 0 underfull boxes, no warnings.** All
fourteen pages rendered at 62 dpi and looked at as contact sheets (`pages/sheet_1.png` to `sheet_4.png`), and the
changed paragraphs on pages 5, 6, 7 and 9 at 105 dpi; nothing runs off the page. Pages whose content changed in this revision:
2, 3, 5, 6, 7, 8, 9, 11, 12, 13; pages 4 and 10 only moved; page 1 is unchanged; page 14 is new (the end of the
bibliography). A first build of this revision had four underfull lines in the "Records" paragraph, which is now a
list.
