# Provenance of "The first L²-Betti number of aspherical manifolds and Poincaré duality groups of dimension at least three" (paper 7, T1)

Written 25 Nov 2026 by the writer of the paper, Claude Fable 5.2 at effort max (agent aee0b161c47a54e8f), on the word of
the main session 329fb1e6 (Claude Opus 5.5 at effort max). Updated the same day after the independent check
(`CHECK_T1_INDEPENDENT.md`) and after the user's paste of the r/math comment. Nothing here was posted, sent or committed.

## Contributors

| Who | What | When |
|---|---|---|
| OpenAI (author line of the manuscript "The Singer conjecture in dimension four") | The method and the whole argument cited as Theorem C: the finite-energy boundary, its convergence action, the tree of cut points, path pushing, the final contradiction (its Sections 3-10); its Section 2 in dimension four | manuscript dated 25 Sep 2026; released in github.com/openai/math on 6 Oct 2026 (its only commit, adc7f124) |
| u/Apprehensive_Sand951 (r/math, thread "AI in mathematics, October 10, 2026", comment pf4k77i) | The observation the paper proves: if OpenAI's proof works, the same method gives that closed aspherical manifolds of dimension ≥ 3 have no L²-harmonic 1-forms; in dimension three this would prove Singer's conjecture without geometrization. Conditional on the manuscript; no proof | thread of 10 Oct 2026 |
| GPT-6 Astra (ChatGPT Pro mode), run Q02 of the batch of open questions | The reductions in every dimension n ≥ 3 (replacement of the manuscript's Section 2), the group criterion, the PD(n)-group form, a reproduction of Sections 3-10 with an inventory of inputs: `pro_batch_20261022_open_questions\answers\Q02-solution.tex` | 22-23 Oct 2026 |
| Claude Opus 5.5 at effort max (Message Batches API) | First referee report on the run: `Q02-check.md` | 23 Oct 2026 |
| Claude Opus 5.5 at effort high (agent a24b3bc642b5dfddf) | Check of five lemmas of the run's Section 2 and of Bowditch's Lemma 1.4 at its statement: `INTAKE_Q02_20261124_CHECK_EVENTS.tsv` | 24 Nov 2026 |
| Claude Fable 5.2 at effort max (agent aee0b161c47a54e8f) | Referee of Sections 3-10 in two stages (`CONFERENCE\Q02_REFEREE_STAGE1.md`, `Q02_REFEREE_STAGE2.md`); check of the three remaining parts of Section 2; writer of this paper; applied the repairs | 25 Nov 2026 |
| Claude Opus 5.5 at effort high (agent a24b3bc642b5dfddf) | Independent check of the finished paper: `CHECK_T1_INDEPENDENT.md`, 23 events (`CHECK_T1_INDEPENDENT_CHECK_EVENTS.tsv`), ten repairs R1-R10 | 25 Nov 2026 |

No human has proved, written or checked any part. The user pasted the text of the r/math comment into the main session
on 25 Nov 2026, because no agent could open Reddit (`RECORDS_r_math_comment_20261125.md`).

## What in the paper is whose

- **Theorem C and everything behind it:** OpenAI's manuscript. The paper cites it and does not reproduce it. The
  manuscript states its theorem for formal dimension four; the reading "Sections 3-10 prove Theorem C" is ours, and
  Section 3 of the paper says on what it rests.
- **The observation that the method gives every n ≥ 3:** the r/math comment (Section 1.3, second item). The paper says
  plainly that it proves that observation, as Theorem A, on the same condition as the comment (that the manuscript's
  argument is correct). One clause of the comment is quoted (11 words).
- **Section 2 (Lemmas 2.1-2.10), Theorems A and B:** the mathematics is that of the run Q02 (GPT-6 Astra, ChatGPT Pro
  mode). The text is the writer's, written afresh. Differences from the run:
  - L²-Betti numbers are defined through harmonic chains, not through modules over the von Neumann algebra, and
    Lemma 2.7 (comparison) is formulated and proved accordingly;
  - the two facts about the von Neumann dimension that Lemma 2.7 uses are proved in Section 1.1 (the writer's, after
    repair R1);
  - Lemma 2.5 is stated for a splitting (one orbit of edges), which is all Theorem C needs;
  - the proof of Lemma 2.9 cites Wall for the cap product on chains where the run wrote out the signs;
  - the last paragraph of the proof of Lemma 2.10 (b₀ = 0) is the writer's direct argument.
- **Section 3.2 and Table 1** (where the manuscript's Sections 3-10 call on its Section 2; the inputs of its 38
  statements): the writer's, from the two referee stages, corrected in five rows by the independent check.
- **Not in the paper:** the consequence for Osin's Problem 3.3 (appendix of `Q02_REFEREE_STAGE2.md`). See "Decisions
  of scope".

## The repairs of 25 Nov (after the independent check)

The check found no mathematical error and listed ten repairs. What was done with each:

| Repair | Done | How |
|---|---|---|
| R1 (Section 1.1: the dimension facts, so that the unopened Lück locator is not needed) | yes, in a longer form | R1's text still took "the two projections have the same trace" from the book. The paper now proves it: polar decomposition, then the Parseval identity Σ_j‖uδ_{1,j}‖² = Σ_i‖u*δ_{1,i}‖² for an equivariant u, in one display. Checked numerically for S₃. **The display and the sentences around it are the writer's and have not been read by the checker.** |
| R2 (Lemma 2.10, optional) | yes; part b in another form | Part a as given, plus the clause that a homomorphism of projective modules is given by a matrix. Part b: instead of choosing a resolution that begins with a Cayley graph, the paper proves b₀ = 0 directly for any projective resolution (last paragraph of the proof). **That paragraph is the writer's and has not been read by the checker.** |
| R3 (proof of Theorem A: Spanier's duality map) | yes, one word changed | "corresponds to cap product" in place of "is cap product": the writer has not opened Spanier's paper, and the check file does not say in which direction its map runs. |
| R4 (abstract: dated 25 Sep, released 6 Oct) | yes | Also in Section 6 and in reference [10]. |
| R5 (Table 1, five rows) | yes, with the optional row 6.3 | Each correction was first read by the writer in the manuscript's source (`dynamics.tex` l.160-170, 242-249; `pretree.tex` l.164-165, 391-395; `blocks.tex` l.333-336; `path-pushing.tex` l.324). |
| R6 (Section 3.3: Lemma 6.2 and Proposition 6.4 of Bowditch's memoir; "no infinite torsion subgroup"; Lemma 1.4's conclusion) | yes | The parenthesis reads "quoted after statement 4.3 and used from statement 4.5 on". Both statements had been opened in stage one; leaving them out was the writer's oversight. |
| R7 (Section 3.4, optional: "Sections 3, 4, 5, 7 and 8 agree sentence for sentence") | **not as worded** | The writer's sentence comparison in both directions shows: Sections 3, 7, 8 identical; in Section 4 the reproduction adds one sentence (l.1533-1535); in Section 5 it replaces the last sentence of the proof of 5.3 by six sentences that spell the step out. Section 3.4 now states the differences. |
| R8 (Lott-Lück is for orientable manifolds) | yes | As given. |
| R9 (the credit to the r/math comment) | yes, as amended by the main session | After the user's paste: the conditional observation with one quoted clause, the dimension-three remark, "gives no proof", and "This paper proves that observation, as Theorem A". Reference [11] now gives the comment's id. |
| R10 (Section 7, item 2, optional) | yes, reworded | Says what the check file records: the proof of Lemma 1.4 has been read; the R-tree construction (Levitt; Bowditch) and Tukia's theorem are not opened; Bestvina-Feighn is opened at its statement. The clause "the rest of its proof is immediate" was not taken over: in the line case of Bestvina-Feighn's Theorem 9.5 the group is free abelian and needs its own argument. |

Also changed: Section 3.4 names the third reader; Section 6 (Sources, Checks) and Section 7 (item 3) describe the
check; the third column of Table 1 is set ragged right.

## Decisions of scope

- **A paper that cites, not a reproduction.** The rule is that a paper proves every new result in full and cites known
  results at the statement used. The manuscript's Sections 3-10 are OpenAI's; the new results are the reductions in
  dimension n and the theorems that follow. So Section 2 is proved in full and Sections 3-10 are cited, with the exact
  interface.
- **Licence.** The repository `openai/math` is under the Apache License 2.0 (checked through the GitHub API on
  25 Nov 2026: `spdx_id` Apache-2.0, file `LICENSE`). This paper is CC0, so it quotes no text of the manuscript beyond
  short phrases and names of objects; every description of a statement of the manuscript is in the writer's words.
- **The Osin consequence is left for a later note.** Reason: it is a different statement for a different audience
  (geometric group theory); it rests on Sections 3-4 only; it has no second reader; and it needs its own literature
  search. An unchecked part inside this paper would blur what the check record covers. The paper has one remark
  (5.3) that Sections 3-4 use neither the vanishing of H² nor the absence of splittings.
- **No claim about the degrees 2, …, n−2**, and no claim for PD(n) groups that are not finitely presented.

## Citations: where each was confirmed

"The checker" is a24b3bc642b5dfddf (Claude Opus 5.5 at effort high), 25 Nov 2026; "the writer" is aee0b161c47a54e8f
(Claude Fable 5.2 at effort max).

| Ref. | Used for | Confirmed |
|---|---|---|
| [10] OpenAI | Theorem C; Section 3 | The writer: source files (`SOURCES.zip` of task Q02; same git blob hashes as the public repository); Sections 3-10 read in full in the run's reproduction and compared with the source. The checker: `paper.pdf` and `build/*.tex` fetched through the GitHub API; the numbers 2.1-2.7 and 3.1-10.3 and every description in Table 1 confirmed in the PDF. The proofs of its Section 2 were not read by the writer (the paper replaces them). |
| [1] Bowditch, Connectedness | Lemma 1.4 | Statement: author manuscript p.6 (`Documents\Free or receipted\free\authors\bowditch\bhb-connected.pdf`), by a24b3bc642b5dfddf on 24 Nov and by the writer. Proof (pp. 3-6, with Lemmas 1.1-1.3): read in full by the checker. Its inputs: Bestvina-Feighn, Invent. Math. 121 (1995), Theorem 9.5, opened by the checker at the statement (GDZ scan, p. 288); **not opened:** Levitt 1998, Bowditch (Topology 1998), Tukia 1994. |
| [2] Bowditch, Treelike structures | Theorem 6.1, Lemma 6.2, Proposition 6.4 and the list in Section 3.3 | Each statement opened by the writer in the author manuscript (`bhb-treelike.pdf`, same folder), pages 29, 30, 36, 40, 41-44, 50, 51, 52, 54, 55, 56-63. Proofs not examined, except that the proof of Theorem 6.1 (p.62-63) was read beside the manuscript's statement 6.4. |
| [7] Kamiya | Moore's arc theorem | Opened by the writer, J-STAGE, p.301-304. |
| [13] Wall | Definition of Poincaré complexes; cap product on chains (Section 1); Lemma 4.1 (two-ended groups) | Opened by the checker (Ranicki's archive, scan of Ann. Math. 86): Section 1, pp. 214-215, with Lemma 1.1 and its chain-level proof; Lemma 4.1, p. 231. Matches. |
| [9] Lück | A pointer for the theory of the von Neumann dimension (Section 1.1); Dodziuk's L² Hodge-de Rham theorem (Section 1.3, to read the comment's "no L²-harmonic 1-forms" as b₁ = 0 for smooth manifolds) | **Not opened by any reader of ours** (the book is not free; the author's site refused the connection on 25 Nov). Chapter-level locator from the writer's memory. No theorem or lemma of the paper depends on it: the two dimension facts are proved in Section 1.1. |
| [8] Lott-Lück, Theorem 0.1 | context (dimension three) | Opened by the checker (GDZ scan of Invent. Math. 120, p. 16; MPIM preprint 92-81): stated for orientable manifolds, hence R8. |
| [4] Davis-Okun, Theorem 11.3.2 | context (right-angled Coxeter groups) | Opened by the checker (arXiv math/0102104v1, p. 53). Matches. |
| [3] Davis, Poincaré duality groups | definition; Theorem 7.15 | Opened by the checker (Ranicki's archive): Definitions 3.1, 3.2, Theorem 3.3 (p. 172), Theorem 7.15. Matches; pages 167-193 confirmed. |
| [5] Di Cerbo-Hunter-Thrasher | context (degree one described as open) | Opened by the checker (arXiv:2601.08804v1): the sentence is in the introduction and again in its Section 3. Matches. |
| [6] Hanner, [14] West, [12] Spanier | topological manifolds are finite Poincaré complexes | Opened by the checker: Hanner p. 392 (Theorems 3.2, 3.3) and West p. 13 ((5.3) Corollary) in Ranicki's archive; Spanier pp. 197-198 (Theorem 10.2, Remark 10.3) at MSP. Match, with the identifications of R3 for Spanier. |
| [11] the r/math comment | credit | **Read from the user's paste of 25 Nov 2026** into the main session (`RECORDS_r_math_comment_20261125.md`; httppf4k77i). No agent of ours could open Reddit: automated access is blocked and the built-in browser refuses reddit.com. |

## Search for later work (25 Nov 2026, by the writer)

- **Hexagon catalogue** (`hexagonmath.org/api/v1/works`, all 16 pages, 1,560 works): keyword filter on title and
  abstract (Singer, Betti, aspherical, acylindrical, convergence group, Osin, finite-energy, Poincaré duality group,
  Hopf conjecture): seven hits, none on the subject.
- **github.com/openai/math:** no issue or pull request mentions Singer; the preprint directory is unchanged (one
  commit, 6 Oct 2026); the repository was updated on 24-25 Nov with other manuscripts.
- **arXiv API**, newest first, six queries ("Singer conjecture"; first L²-Betti number and aspherical; finite-energy
  boundary; acylindrically hyperbolic and Betti number; Poincaré duality group and L²-Betti; titles with Singer,
  conjecture, dimension): nothing after 6 Oct 2026 on the manuscript or an extension; nothing that settles Osin's
  Problem 3.3.
- **Web search**, standard mode, two queries: nothing on the manuscript, an extension, or a solution of Osin's
  problem.
- Limits: keyword searches. Reddit, MathOverflow and blogs were not searched by the writer; `OLDER_RUNS.md` records
  the main session's extended searches of 24 Nov.

## Still open before posting

1. **A second reader of Sections 8 and 9 of the manuscript** (826 lines in the reproduction), from another model
   family. They carry the theorem; only the writer has read them line by line.
2. **The inputs of Bowditch's Lemma 1.4.** Its proof has now been read (the checker). Not opened: the construction of
   an R-tree from a minimal convergence action on a dendrite (Levitt 1998; Bowditch, Topology 1998) and Tukia 1994.
   Bestvina-Feighn's Theorem 9.5 is opened at its statement only.
3. **A second reading of what the writer wrote after the check.** The mathematical passages are:
   - Section 1.1, from "Indeed, the dimension equals" to the display and the sentence after it (pp. 1-2);
   - the last paragraph of the proof of Lemma 2.10, "Finally b₀ = 0 …" (p. 7).

   The others are wording: the credit item in Section 1.3 (p. 3), the clause on Spanier in the proof of Theorem A
   (p. 11), the parenthesis in Section 3.3 (p. 10), Section 3.4 (p. 11), Section 6 (p. 12), item 2 of Section 7
   (p. 13).
4. **Two sources not opened by any agent:** Lück's book (chapter-level locator; it carries Dodziuk's theorem for the
   credit paragraph) and the r/math comment at its address (read from the user's paste).
5. **A wider search** for discussion of the manuscript since 6 Oct 2026 (Reddit, MathOverflow, blogs), and a human
   reader who knows convergence groups, if one can be found.
6. **The user's word**, and every page read by the main session. Hexagon metadata is not prepared.

## Files

- `T1_paper.pdf` (14 pages; built from a clean state three times with pdflatex; 0 overfull and 0 underfull boxes;
  every page rendered at 80 dpi and looked at: `pages\`).
- `src\T1_paper.tex`, with `build1.txt` to `build3.txt` and the log.
- `ABSTRACT.md`, `PROVENANCE.md`, `CHECK_EVENTS.tsv` (108 rows: the five of 24 Nov, the 36 and 23 of the two referee
  stages, 12 for the first version of this paper, the checker's 23, and 9 for the repairs).
- `CHECK_T1_INDEPENDENT.md` and `CHECK_T1_INDEPENDENT_CHECK_EVENTS.tsv` (the independent check);
  `RECORDS_r_math_comment_20261125.md` (record of the comment, not for publication).
- Referee reports: `..\..\Q02_REFEREE_STAGE1.md`, `..\..\Q02_REFEREE_STAGE2.md`; work file
  `aee0b161c47a54e8f_NOTES.md`.

## The main session's reading (329fb1e6, Claude Opus 5.5 at effort max), 25 Nov 2026 ~06:10-06:20 UTC

- Every page of the repaired build read (`pages_main\`, 100 dpi), every proof of Section 2 followed, including the two
  passages written after the independent check (the Parseval identity in Section 1.1; "Finally b_0 = 0" in the proof of
  Lemma 2.10): both hold. Item 3 of the list above is done; item 6 is done except the user's word and the metadata.
- Corrected: Section 3.3 described Bowditch's Theorem 6.1 (Treelike structures) with the hypothesis "with no infinite
  torsion subgroup", inserted by the checker's R6. Bowditch's statement (author's manuscript, Section 6, `Free or
  receipted/free/authors/bowditch/bhb-treelike.pdf`) has no such hypothesis: "Suppose that Γ is a one-ended finitely
  generated group which admits a minimal convergence action on a continuum, M. If M has a cut point which is not a
  parabolic fixed point, then the quotient D(M) is non-trivial"; the torsion condition is in his introduction and in
  the remark after the statement only. The referee's stage two had said the same (`Q02_REFEREE_STAGE2.md`, l.186-187).
  The clause is removed; Section 6 now says so. Lemma 1.4 of [1] does carry the torsion hypothesis (`bhb-connected.pdf`,
  Section 1), and its "parabolic on D" is Bowditch's "fixes a point" (his definition before the lemma), so the first
  bullet stands.
- Checked: the comment [11] existed by 11 Oct 2026 02:30 UTC (the user's record of the thread), so it
  is earlier than the run of 22-23 Oct, as Section 6 says; the thread title is from the user's paste (P1150).
- Checked: the reproduction's rewrite of the limit argument at the end of 9.8 was compared with the manuscript's own
  argument by the referee, who calls both correct (`Q02_REFEREE_STAGE2.md`, l.19-21 and 190).
- Backup before these edits: `src\T1_paper_before_main_bowditch61_fix_20261125.tex`. Rebuilt three times: 14 pages,
  0 overfull, 0 underfull, no undefined references; pages 10-14 read again.
