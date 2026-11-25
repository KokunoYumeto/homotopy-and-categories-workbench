# d2_examples_check.py -- checks for the two examples of the paper
# "Classifying spaces of finite monoids with bounded homology" (D2).
# Written by afceadd46f7598ec4 (Claude Fable 5.2 at effort max), 25 Nov 2026; independent of the programs of the runs.
# Exact integer arithmetic (python-flint for ranks and Smith normal forms).
import itertools
import flint


class Mon:
    def __init__(self, elems, mul, one):
        self.E = list(elems)
        self.n = len(self.E)
        self.ix = {x: i for i, x in enumerate(self.E)}
        self.T = [[self.ix[mul(a, b)] for b in self.E] for a in self.E]      # KeyError if not closed
        self.one = self.ix[one]
        for a in range(self.n):
            assert self.T[self.one][a] == a and self.T[a][self.one] == a
            for b in range(self.n):
                for c in range(self.n):
                    assert self.T[self.T[a][b]][c] == self.T[a][self.T[b][c]]

    def vec(self, d):
        v = [0] * self.n
        for k, c in d.items():
            v[self.ix[k]] += c
        return v

    def unit(self, i):
        v = [0] * self.n
        v[i] = 1
        return v

    def prod(self, x, y):
        z = [0] * self.n
        for i, a in enumerate(x):
            if a:
                for j, b in enumerate(y):
                    if b:
                        z[self.T[i][j]] += a * b
        return z


def snf_diag(rows):
    A = flint.fmpz_mat(len(rows), len(rows[0]), [x for r in rows for x in r]).snf()
    return [abs(int(A[i, i])) for i in range(min(A.nrows(), A.ncols())) if int(A[i, i]) != 0]


def check_resolution(M, mods, maps, top_injective, label):
    """mods[k] = list of idempotents of ZM (the summands R.eps of P_k); maps[k] (k >= 1) = list over the summands i
    of P_k of tuples (w_ij)_j, the image of the generator eps_i in P_{k-1}.  Checks: the generators are idempotent;
    the images lie in the target and are fixed by the source idempotent; d d = 0; aug d_1 = 0; exactness over Z by
    ranks and saturation of the images."""
    Z = [0] * M.n
    for mod in mods:
        for eps in mod:
            assert M.prod(eps, eps) == eps

    def span(k):
        out = []
        for j, eps in enumerate(mods[k]):
            for m in range(M.n):
                y = [Z] * len(mods[k])
                y[j] = M.prod(M.unit(m), eps)
                out.append(tuple(tuple(part) for part in y))
        return out

    def apply(k, y):                       # d_k : P_k -> P_{k-1}
        res = [list(Z) for _ in mods[k - 1]]
        for i, yi in enumerate(y):
            if any(yi):
                for j, w in enumerate(maps[k][i]):
                    p = M.prod(yi, w)
                    res[j] = [a + b for a, b in zip(res[j], p)]
        return tuple(tuple(r) for r in res)

    def flat(y):
        return [c for part in y for c in part]

    for k in range(1, len(mods)):
        for i, eps in enumerate(mods[k]):
            for j, w in enumerate(maps[k][i]):
                assert M.prod(eps, w) == w and M.prod(w, mods[k - 1][j]) == w
    rk, im = [], [1]
    assert any(abs(sum(flat(y))) == 1 for y in span(0))
    for k in range(len(mods)):
        S = span(k)
        d = snf_diag([flat(y) for y in S])
        assert all(x == 1 for x in d)
        rk.append(len(d))
        if k >= 1:
            images = [apply(k, y) for y in S]
            d = snf_diag([flat(y) for y in images])
            assert all(x == 1 for x in d), "image not saturated"
            im.append(len(d))
            for y in images:
                if k == 1:
                    assert sum(flat(y)) == 0
                else:
                    assert not any(flat(apply(k - 1, y)))
    for k in range(len(mods) - 1):
        assert rk[k] == im[k] + im[k + 1], (k, rk, im)
    if top_injective:
        assert rk[-1] == im[-1]
    print("%s: Z-ranks of the modules %s; ranks of (aug, d_1, ...) %s; all images saturated; exact%s"
          % (label, rk, im, " and the top map injective" if top_injective else " below the top term"))


def bar_boundary(M, chain):               # trivial coefficients, normalized bar complex
    out = {}

    def add(k, c):
        if M.one in k:
            return
        out[k] = out.get(k, 0) + c

    for c, coef in chain.items():
        n = len(c)
        add(c[1:], coef)
        for i in range(1, n):
            add(c[:i - 1] + (M.T[c[i - 1]][c[i]],) + c[i + 1:], (-1) ** i * coef)
        add(c[:-1], (-1) ** n * coef)
    return {k: v for k, v in out.items() if v}


# ---------------------------------------------------------------- M_6
names6 = ["1", "x00", "x01", "x10", "x11", "y"]
row = {"x00": 0, "x01": 0, "x10": 1, "x11": 1, "y": 0}
col = {"x00": 0, "x01": 1, "x10": 0, "x11": 1, "y": 0}


def mul6(v, w):
    if v == "1":
        return w
    if w == "1":
        return v
    return "x%d%d" % (row[v], col[w])


M6 = Mon(names6, mul6, "1")
e = M6.vec({"x00": 1})
u = M6.vec({"1": 1, "x00": -1})
a = M6.vec({"x10": 1, "x00": -1})
b = M6.vec({"x01": 1, "x00": -1})
t = M6.vec({"y": 1, "x00": -1})
Z6 = [0] * 6
check_resolution(M6, [[e], [u], [e, u], [e, u], [e, u]],
                 [None, [(a,)], [(b,), (t,)], [(Z6, b), (Z6, t)], [(Z6, b), (Z6, t)]], False,
                 "M_6 (periodic resolution, degrees 0..4)")
I6 = M6.ix


def alpha(m):
    return 1 if (m != I6["1"] and col[names6[m]] == 1) else 0


def beta(m):
    return 1 if (m != I6["1"] and row[names6[m]] == 1) else 0


def Yf(m):
    return 1 if m == I6["y"] else 0


def f(n, c):
    v = alpha(c[0]) * beta(c[-1])
    for m in c[1:-1]:
        v *= Yf(m)
    return v


non1 = [i for i in range(6) if i != I6["1"]]
for n in range(2, 6):
    pairs = [(I6["x01"], I6["x00"])] + [(I6["y"], I6["x00"])] * (n - 2) + [(I6["x10"], I6["x00"])]
    z = {}
    for epsb in itertools.product((0, 1), repeat=n):
        k = tuple(pairs[i][epsb[i]] for i in range(n))
        z[k] = z.get(k, 0) + (-1) ** sum(epsb)
    assert bar_boundary(M6, z) == {}
    for c in itertools.product(non1, repeat=n + 1):          # delta f_n = 0 on all (n+1)-tuples
        d = f(n, c[1:]) + (-1) ** (n + 1) * f(n, c[:-1])
        for i in range(1, n + 1):
            d += (-1) ** i * f(n, c[:i - 1] + (M6.T[c[i - 1]][c[i]],) + c[i + 1:])
        assert d == 0
    assert sum(coef * f(n, k) for k, coef in z.items()) == 1
print("M_6: for n = 2..5, z_n is a cycle, f_n is a cocycle, <f_n, z_n> = 1")

# ---------------------------------------------------------------- M_23
ident = ((0, 1, 2), (0, 1, 2, 3, 4))


def P(s, tt):
    return (tuple(int(ch) for ch in s), tuple(int(ch) for ch in tt))


named = {"1": ident, "a": P("002", "02200"), "b": P("002", "41144"), "c": P("010", "04034"),
         "d": P("202", "03300"), "e": P("202", "12211"), "f": P("202", "40044"), "g": P("212", "00334")}
for i in range(3):
    for j in range(5):
        named["x%d%d" % (i, j)] = ((i,) * 3, (j,) * 5)
inv = {v: k for k, v in named.items()}
assert len(inv) == 23


def mul23(p, q):
    s = tuple(named[p][0][named[q][0][i]] for i in range(3))        # sigma_p o sigma_q
    tt = tuple(named[q][1][named[p][1][j]] for j in range(5))       # tau_q o tau_p
    return inv[(s, tt)]


order = ["1"] + ["x%d%d" % (i, j) for i in range(3) for j in range(5)] + list("abcdefg")
M = Mon(order, mul23, "1")
V = M.vec
for nm in "abcg":
    assert mul23(nm, nm) == nm
assert (mul23("d", "d"), mul23("e", "e"), mul23("f", "f")) == ("x20", "x22", "x24")
assert all(M.T[m][n] != M.one for m in range(23) for n in range(23) if m != M.one and n != M.one)
x00 = V({"x00": 1})
cm = V({"c": 1, "x00": -1})
om = V({"1": 1, "c": -1})
am = V({"a": 1, "x00": -1})
Z = [0] * 23
mods = [[x00], [cm], [x00, om], [am, am], [x00]]
maps = [None,
        [(V({"x10": 1, "x00": -1}),)],
        [(V({"x03": 1, "x00": -1}),), (V({"c": 1, "d": 1, "g": -1, "x00": -1}),)],
        [(V({"x00": 1, "x20": -1}), V({"b": 1, "e": 1, "f": -1, "x01": -1})), (Z, am)],
        [(V({"x02": 1, "x00": -1}), V({"x02": -1, "x00": 1}))]]
check_resolution(M, mods, maps, True, "M_23 (resolution of length 4)")
print("M_23: augmentations of the generating idempotents:", [[sum(eps) for eps in mod] for mod in mods])
L = {0: (0, 0, 0), 1: (0, 1, 1), 2: (0, 0, 1), 3: (0, -1, 0), 4: (0, 1, 0)}
sig0 = [named[nm][0][0] for nm in order]
tau0 = [named[nm][1][0] for nm in order]


def uc(m, n):
    return L[tau0[m]][sig0[n]]


for m in range(23):
    assert uc(M.one, m) == 0 and uc(m, M.one) == 0
    for n in range(23):
        for k in range(23):
            assert uc(n, k) - uc(M.T[m][n], k) + uc(m, M.T[n][k]) - uc(m, n) == 0


def lmul(r, chain):
    out = {}
    for x, cx in enumerate(r):
        if cx:
            for key, c in chain.items():
                k2 = (M.T[x][key[0]],) + key[1:]
                out[k2] = out.get(k2, 0) + cx * c
    return {k: v for k, v in out.items() if v}


def s_op(chain):
    return {(M.one,) + key: c for key, c in chain.items() if key[0] != M.one}


def left_boundary(chain):                 # differential of the normalized left bar resolution
    out = {}

    def add(k, c):
        if M.one in k[1:]:
            return
        out[k] = out.get(k, 0) + c

    for key, coef in chain.items():
        zz, ms = key[0], key[1:]
        n = len(ms)
        add((M.T[zz][ms[0]],) + ms[1:], coef)
        for i in range(1, n):
            add((zz,) + ms[:i - 1] + (M.T[ms[i - 1]][ms[i]],) + ms[i + 1:], (-1) ** i * coef)
        add((zz,) + ms[:-1], (-1) ** n * coef)
    return {k: v for k, v in out.items() if v}


Tg = {(0, 0): {(M.one,): 1}}


def Fmap(k, i, y):                        # F_k on an element y = y eps_i of the i-th summand of P_k
    return lmul(y, Tg[(k, i)])


for k in range(1, 5):
    for i, eps in enumerate(mods[k]):
        ch = {}
        for j, w in enumerate(maps[k][i]):
            if any(w):
                for kk, v in Fmap(k - 1, j, w).items():
                    ch[kk] = ch.get(kk, 0) + v
        ch = {kk: v for kk, v in ch.items() if v}
        Tg[(k, i)] = s_op(ch)
        assert left_boundary(Fmap(k, i, eps)) == ch, (k, i)     # d F_k(eps) = F_{k-1}(d_k eps)


def aug(chain):
    out = {}
    for key, v in chain.items():
        out[key[1:]] = out.get(key[1:], 0) + v
    return {k: v for k, v in out.items() if v}


z2 = aug(Fmap(2, 0, x00))
z4 = aug(Fmap(4, 0, x00))
assert bar_boundary(M, z2) == {} and bar_boundary(M, z4) == {}
p2 = sum(v * uc(k[0], k[1]) for k, v in z2.items())
p4 = sum(v * uc(k[0], k[1]) * uc(k[2], k[3]) for k, v in z4.items())
print("M_23: u is a normalized 2-cocycle; the comparison map is a chain map in degrees 1..4; numbers of terms of"
      " F_k(generator):", {k: len(Fmap(k[0], k[1], mods[k[0]][k[1]])) for k in sorted(Tg)})
print("M_23: <u, z_2> = %d, <u cup u, z_4> = %d  (z_2, z_4: cycles, images of the generators of Z (x) P_2 and"
      " Z (x) P_4)" % (p2, p4))
assert abs(p2) == 1 and abs(p4) == 1
print("ALL CHECKS PASSED")
