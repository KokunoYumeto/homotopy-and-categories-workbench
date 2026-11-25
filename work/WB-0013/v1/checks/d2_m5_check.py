# Check of the paragraph "The monoid with five elements" of the paper
# "Classifying spaces of finite monoids with bounded homology" (D2), Section 5.
# Written 25 Nov 2026 by afceadd46f7598ec4 (Claude Fable 5.2 at effort max).
# Exact integer arithmetic, standard library only. Run: python -I -B d2_m5_check.py
#
# M5 = {1, x00, x01, x10, x11}, x_ij x_kl = x_il (Fiedorowicz 1984, p. 323, with indices 0, 1).
# Checked here:
#  (1) M5 is a monoid;
#  (2) e, u, a, b, c is a Z-basis of R' = Z M5, with the products used in the paper;
#  (3) R'e = Ze + Za, R'u = Zu + Zb + Zc;
#  (4) 0 -> R'e -(s -> sb)-> R'u -(s -> sa)-> R'e -(eps)-> Z -> 0 is exact;
#  (5) the augmentations of e and u are 1 and 0 (so the homology is Z, 0, Z);
#  (6) z_2 is a cycle and f_2 a cocycle of the cellular chain complex of BM5, and f_2(z_2) = 1;
#  (7) independently of the resolution: H_1, H_2, H_3 of the normalized bar complex of M5 are 0, Z, 0.

import itertools

ok = True


def check(name, cond):
    global ok
    print(("ok    " if cond else "FAIL  ") + name)
    if not cond:
        ok = False


ELEMS = ["1", "x00", "x01", "x10", "x11"]
NONID = ELEMS[1:]


def mul(v, w):
    if v == "1":
        return w
    if w == "1":
        return v
    return "x" + v[1] + w[2]


# (1) monoid
check("closed", all(mul(v, w) in ELEMS for v in ELEMS for w in ELEMS))
check("identity", all(mul("1", v) == v and mul(v, "1") == v for v in ELEMS))
check("associative", all(mul(mul(x, y), z) == mul(x, mul(y, z))
                         for x in ELEMS for y in ELEMS for z in ELEMS))
check("x_ij x_kl = x_il", all(mul("x%d%d" % (i, j), "x%d%d" % (k, l)) == "x%d%d" % (i, l)
                              for i in (0, 1) for j in (0, 1) for k in (0, 1) for l in (0, 1)))
check("products of non-identity elements are non-identity",
      all(mul(v, w) != "1" for v in NONID for w in NONID))


# group ring elements: dicts element -> integer
def clean(p):
    return {k: v for k, v in p.items() if v != 0}


def add(p, q, s=1):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + s * v
    return clean(r)


def rmul(p, q):
    r = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = mul(k1, k2)
            r[k] = r.get(k, 0) + v1 * v2
    return clean(r)


def el(name):
    return {name: 1}


def aug(p):
    return sum(p.values())


ONE = el("1")
e = el("x00")
u = add(ONE, e, -1)
a = add(el("x10"), e, -1)
b = add(el("x01"), e, -1)
c = add(add(add(el("x11"), el("x10"), -1), el("x01"), -1), e)
ZERO = {}


def coords(p):
    # coordinates in the basis (e, u, a, b, c), from 1 = u + e, x00 = e, x10 = a + e,
    # x01 = b + e, x11 = c + a + b + e
    n1, n00, n01, n10, n11 = (p.get(k, 0) for k in ELEMS)
    return (n1 + n00 + n01 + n10 + n11, n1, n10 + n11, n01 + n11, n11)


def from_coords(v):
    r = {}
    for coef, basis in zip(v, (e, u, a, b, c)):
        r = add(r, {k: coef * val for k, val in basis.items()})
    return r


# (2) basis and products
check("e, u, a, b, c is a Z-basis (inverse substitution reproduces every element)",
      all(from_coords(coords(el(m))) == el(m) for m in ELEMS))
check("coordinates of e, u, a, b, c are the unit vectors",
      [coords(x) for x in (e, u, a, b, c)] ==
      [(1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 0, 1)])
check("e, u idempotent, eu = ue = 0",
      rmul(e, e) == e and rmul(u, u) == u and rmul(e, u) == ZERO and rmul(u, e) == ZERO)
check("ae = a, ea = 0, eb = b, be = 0", rmul(a, e) == a and rmul(e, a) == ZERO
      and rmul(e, b) == b and rmul(b, e) == ZERO)
check("ab = c, ba = 0, ua = a, bu = b, cu = c, ca = 0, bb = 0",
      rmul(a, b) == c and rmul(b, a) == ZERO and rmul(u, a) == a and rmul(b, u) == b
      and rmul(c, u) == c and rmul(c, a) == ZERO and rmul(b, b) == ZERO)

# (3) the left ideals R'e and R'u
Re_gens = [coords(rmul(el(m), e)) for m in ELEMS]
Ru_gens = [coords(rmul(el(m), u)) for m in ELEMS]
check("R'e lies in Ze + Za", all(v[1] == 0 and v[3] == 0 and v[4] == 0 for v in Re_gens))
check("R'e contains e and a", coords(rmul(ONE, e)) == (1, 0, 0, 0, 0)
      and coords(add(rmul(el("x10"), e), rmul(el("x00"), e), -1)) == (0, 0, 1, 0, 0))
check("R'u lies in Zu + Zb + Zc", all(v[0] == 0 and v[2] == 0 for v in Ru_gens))
check("R'u contains u, b and c", coords(rmul(ONE, u)) == (0, 1, 0, 0, 0)
      and coords(rmul(el("x01"), u)) == (0, 0, 0, 1, 0)
      and coords(add(rmul(el("x11"), u), rmul(el("x01"), u), -1)) == (0, 0, 0, 0, 1))

# (4) exactness
check("d_1 on the basis u, b, c of R'u: u -> a, b -> 0, c -> 0 (kernel Zb + Zc, image Za)",
      rmul(u, a) == a and rmul(b, a) == ZERO and rmul(c, a) == ZERO)
check("d_2 on the basis e, a of R'e: e -> b, a -> c (injective, image Zb + Zc)",
      rmul(e, b) == b and rmul(a, b) == c)
check("kernel of the augmentation on R'e is Za", aug(e) == 1 and aug(a) == 0)

# (5) augmentations of the generating idempotents
check("augmentation of e is 1, of u is 0", aug(e) == 1 and aug(u) == 0)


# (6) the cycle z_2 and the cocycle f_2
def boundary(cell):
    # cellular boundary of BM5 on a tuple of non-identity elements
    k = len(cell)
    out = {}

    def put(t, s):
        out[t] = out.get(t, 0) + s
    put(cell[1:], 1)
    for i in range(1, k):
        put(cell[:i - 1] + (mul(cell[i - 1], cell[i]),) + cell[i + 1:], (-1) ** i)
    put(cell[:-1], (-1) ** k)
    return {t: s for t, s in out.items() if s != 0}


A = {0: "x01", 1: "x00"}   # (a_1^0, a_1^1)
B = {0: "x10", 1: "x00"}   # (a_2^0, a_2^1)
z2 = {}
for e1 in (0, 1):
    for e2 in (0, 1):
        z2[(A[e1], B[e2])] = (-1) ** (e1 + e2)
dz2 = {}
for cell, s in z2.items():
    for t, s2 in boundary(cell).items():
        dz2[t] = dz2.get(t, 0) + s * s2
check("z_2 is a cycle", all(v == 0 for v in dz2.values()))
check("z_2 lies in BM5 (its cells are pairs of elements x_ij)",
      all(m in NONID for cell in z2 for m in cell))


def alpha(m):
    return 1 if m[2] == "1" else 0


def beta(m):
    return 1 if m[1] == "1" else 0


def f2(m1, m2):
    return alpha(m1) * beta(m2)


check("f_2 is a cocycle on BM5", all(
    f2(m1, m2) - f2(mul(m0, m1), m2) + f2(m0, mul(m1, m2)) - f2(m0, m1) == 0
    for m0 in NONID for m1 in NONID for m2 in NONID))
check("f_2(z_2) = 1", sum(s * f2(*cell) for cell, s in z2.items()) == 1)


# (7) homology of the normalized bar complex in degrees 1, 2, 3, without the resolution
def cells(k):
    return list(itertools.product(NONID, repeat=k))


def boundary_matrix(k):
    src, tgt = cells(k), cells(k - 1)
    index = {t: i for i, t in enumerate(tgt)}
    mat = [[0] * len(src) for _ in tgt]
    for j, cell in enumerate(src):
        for t, s in boundary(cell).items():
            mat[index[t]][j] += s
    return mat


def diagonal_form(mat):
    # diagonalization of an integer matrix by row and column operations;
    # returns the list of non-zero diagonal entries (absolute values)
    m = [row[:] for row in mat]
    diag = []
    while True:
        best = None
        for i, row in enumerate(m):
            for j, x in enumerate(row):
                if x != 0 and (best is None or abs(x) < abs(m[best[0]][best[1]])):
                    best = (i, j)
        if best is None:
            return diag
        i0, j0 = best
        p = m[i0][j0]
        dirty = False
        for i in range(len(m)):
            if i != i0 and m[i][j0] != 0:
                q = m[i][j0] // p
                m[i] = [x - q * y for x, y in zip(m[i], m[i0])]
                if m[i][j0] != 0:
                    dirty = True
        for j in range(len(m[0])):
            if j != j0 and m[i0][j] != 0:
                q = m[i0][j] // p
                for row in m:
                    row[j] -= q * row[j0]
                if m[i0][j] != 0:
                    dirty = True
        if not dirty:
            diag.append(abs(p))
            m = [row[:j0] + row[j0 + 1:] for i, row in enumerate(m) if i != i0]
            if not m or not m[0]:
                return diag


d = {k: diagonal_form(boundary_matrix(k)) for k in (2, 3, 4)}
rank = {k: len(d[k]) for k in d}
torsion_free = {k: all(x == 1 for x in d[k]) for k in d}
print("ranks of the bar differentials d_2, d_3, d_4:", rank[2], rank[3], rank[4])
check("H_1 = 0 (d_1 = 0, rank d_2 = 4, elementary divisors 1)", rank[2] == 4 and torsion_free[2])
check("H_2 = Z (kernel of d_2 has rank 12, rank d_3 = 11, elementary divisors 1)",
      16 - rank[2] == 12 and rank[3] == 11 and torsion_free[3])
check("H_3 = 0 (kernel of d_3 has rank 53, rank d_4 = 53, elementary divisors 1)",
      64 - rank[3] == 53 and rank[4] == 53 and torsion_free[4])

print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
