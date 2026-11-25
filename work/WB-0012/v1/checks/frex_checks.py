"""Finite checks for the paper "Exactness of colimits and amenability are independent ...".
Written by the paper's writer (Claude Fable 5.2 at effort max), 25 Nov 2026, independently of the programs of the run.
Exact integer arithmetic only.  Run:  python -I -B frex_checks.py

(1) Lemma 4.1: the integer weights w_P(pi) on the linear extensions of a finite poset with a reference order:
    total 1 and the one-point restriction identity, for every partial order on at most 5 labelled points
    (the reference order is the order of the labels, so all reference orders are covered).
    The weights are computed in two ways: from the cells (ordered partitions into blocks) and from the
    formula with consecutive blocks.
(2) The three-point example of Remark 4.2 (the weights are not multiplicative).
(3) The proof of Theorem 1.5 (c): the two identities behind the obstruction over F_2, for all injective linear maps
    F_2^3 -> F_2^n and F_2^2 -> F_2^n, n = 3, 4, 5, with the natural order of F_2^n (integer order of bit masks).
"""
from itertools import permutations, product, combinations


# ---------- (1) weights on linear extensions ----------
def partial_orders(n):
    """All strict partial orders on range(n), as frozensets of pairs (a, b) meaning a < b."""
    pairs = [(a, b) for a in range(n) for b in range(n) if a != b]
    seen = set()
    def closure(rel):
        rel = set(rel)
        changed = True
        while changed:
            changed = False
            for (a, b) in list(rel):
                for (c, d) in list(rel):
                    if b == c and (a, d) not in rel:
                        rel.add((a, d)); changed = True
        return rel
    out = set()
    stack = [frozenset()]
    while stack:
        r = stack.pop()
        if r in out:
            continue
        out.add(r)
        for p in pairs:
            if p in r or (p[1], p[0]) in r:
                continue
            c = closure(r | {p})
            if any((a, a) in c or ((b, a) in c) for (a, b) in c):
                continue
            c = frozenset(c)
            if c not in out:
                stack.append(c)
    return out


def ordered_partitions(elems):
    """All ordered partitions (lists of blocks) of the tuple elems."""
    elems = list(elems)
    if not elems:
        yield []
        return
    first, rest = elems[0], elems[1:]
    for part in ordered_partitions(rest):
        for i in range(len(part)):
            yield part[:i] + [part[i] + [first]] + part[i + 1:]
        for i in range(len(part) + 1):
            yield part[:i] + [[first]] + part[i:]


def weights_cells(points, rel):
    """w(pi) = (-1)^n * sum over cells sorting to pi of (-1)^(number of blocks)."""
    n = len(points)
    w = {}
    for part in ordered_partitions(points):
        pos = {}
        for i, blk in enumerate(part):
            for x in blk:
                pos[x] = i
        if any(pos[a] >= pos[b] for (a, b) in rel):
            continue
        pi = tuple(x for blk in part for x in sorted(blk))
        w[pi] = w.get(pi, 0) + (-1) ** (n + len(part))
    return w


def weights_formula(points, rel):
    """The formula of the run: consecutive blocks that are antichains listed increasingly."""
    n = len(points)
    w = {}
    for pi in permutations(points):
        idx = {x: i for i, x in enumerate(pi)}
        if any(idx[a] > idx[b] for (a, b) in rel):
            continue
        total = 0
        for cuts in product([0, 1], repeat=max(n - 1, 0)):
            blocks, cur = [], [pi[0]] if n else []
            for i in range(1, n):
                if cuts[i - 1]:
                    blocks.append(cur); cur = [pi[i]]
                else:
                    cur.append(pi[i])
            if n:
                blocks.append(cur)
            ok = True
            for blk in blocks:
                if list(blk) != sorted(blk):
                    ok = False
                if any((a, b) in rel or (b, a) in rel for a, b in combinations(blk, 2)):
                    ok = False
            if ok:
                total += (-1) ** (n + len(blocks))
        w[pi] = total
    return w


def check_weights(nmax=5):
    count = 0
    eqs = 0
    for n in range(0, nmax + 1):
        pts = tuple(range(n))
        for rel in partial_orders(n):
            w = weights_cells(pts, rel)
            if n <= 4:
                w2 = weights_formula(pts, rel)
                assert {k: v for k, v in w2.items()} == {k: w.get(k, 0) for k in w2}, (n, rel)
            assert sum(w.values()) == 1, (n, rel)
            for x in pts:
                sub = tuple(p for p in pts if p != x)
                subrel = frozenset((a, b) for (a, b) in rel if a != x and b != x)
                wq = weights_cells(sub, subrel)
                acc = {}
                for pi, v in w.items():
                    tau = tuple(p for p in pi if p != x)
                    acc[tau] = acc.get(tau, 0) + v
                for tau in set(acc) | set(wq):
                    assert acc.get(tau, 0) == wq.get(tau, 0), (n, rel, x, tau)
                    eqs += 1
            count += 1
    return count, eqs


def check_example():
    wq = weights_cells((0, 1), frozenset())
    assert wq.get((0, 1), 0) == 0 and wq.get((1, 0), 0) == 1
    # x = 0, y = 1, z = 2 ; x below z in the partial order
    wp = weights_cells((0, 1, 2), frozenset({(0, 2)}))
    assert wp.get((0, 1, 2), 0) == -1 and wp.get((0, 2, 1), 0) == 1 and wp.get((1, 0, 2), 0) == 1
    return wq, wp


# ---------- (3) the obstruction over F_2 ----------
REF = [1, 2, 3, 4, 6, 5, 7]                      # reference order of Q = F_2^3 minus 0
TRIPLES = [(1, 2, 3), (1, 6, 7), (2, 5, 7), (3, 4, 7), (3, 6, 5)]


def injective_linear_maps(r, n):
    """Injective linear maps F_2^r -> F_2^n as dicts on the non-zero vectors 1..2^r-1 (bit masks)."""
    for imgs in product(range(1, 2 ** n), repeat=r):
        m = {}
        for v in range(1, 2 ** r):
            x = 0
            for i in range(r):
                if v >> i & 1:
                    x ^= imgs[i]
            m[v] = x
        if all(x != 0 for x in m.values()) and len(set(m.values())) == len(m):
            yield m


def check_f2():
    rank = {v: i for i, v in enumerate(REF)}
    for t in TRIPLES:
        assert t[0] ^ t[1] == t[2]
        assert rank[t[0]] < rank[t[1]] < rank[t[2]]
    def between(a, b, c):                       # b strictly between a and c
        return (a < b < c) or (c < b < a)
    n_g = n_e = 0
    for n in (3, 4, 5):
        for g in injective_linear_maps(3, n):
            img = [tuple(g[v] for v in t) for t in TRIPLES]
            s = (img[0][1] < img[0][0]) + (img[1][0] < img[1][1]) + (img[2][0] < img[2][1]) \
                + between(img[3][0], img[3][1], img[3][2]) + (img[4][2] < img[4][1])
            assert s % 2 == 0
            n_g += 1
        for e in injective_linear_maps(2, n):
            # x1, x2, x3 = the non-zero vectors 1, 2, 3 of F_2^2 in any fixed order: all three bijections are linear
            for (p1, p2, p3) in permutations((1, 2, 3)):
                x1, x2, x3 = e[p1], e[p2], e[p3]
                s = (x2 < x1) + 2 * (x1 < x2) + between(x1, x2, x3) + (x3 < x2)
                assert s % 2 == 1
                n_e += 1
    return n_g, n_e


if __name__ == '__main__':
    c, eqs = check_weights(5)
    print('weights: %d partial orders on at most 5 labelled points, %d restriction equations, totals all 1' % (c, eqs))
    wq, wp = check_example()
    print('example: antichain {x<y}:', wq, '| with z above x:', wp)
    ng, ne = check_f2()
    print('F_2: %d maps g of F_2^3 give sum 0 mod 2; %d ordered embeddings of F_2^2 give sum 1 mod 2' % (ng, ne))
    print('ALL CHECKS PASSED')
