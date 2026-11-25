"""Independent small-target check of TOTEX2 A.1/A.3 (C_delta: no affine equalizer of v1,v2,v3: V -> W).
Written by Claude Opus 5.5 at effort high (agent a24b3bc642b5dfddf), 24 Nov 2026, from the statement of A.1 only.
For every object X = ([n], E) of C_delta with n <= NMAX, list the arrows W -> X and V -> X and decide whether
sum_g t_g = 1 and sum_{g} t_g [g v_1] = sum_g t_g [g v_2] = sum_g t_g [g v_3] has a solution over Q, F_2, F_3, F_5.
A solution for some X would refute A.1/A.3; none is expected."""
import itertools, sys
from fractions import Fraction
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7

def delta(E, U):
    U = set(U)
    return 2*len(U) - 3*sum(1 for e in E if set(e) <= U)

def is_object(n, E):
    pts = range(n)
    for k in range(1, n+1):
        for U in itertools.combinations(pts, k):
            if delta(E, U) <= 0: return False
    return True

def strictly_closed(n, E, S):
    dS = delta(E, S)
    rest = [p for p in range(n) if p not in S]
    for k in range(1, len(rest)+1):
        for extra in itertools.combinations(rest, k):
            if delta(E, set(S) | set(extra)) <= dS: return False
    return True

def solvable(rows, rhs, field):
    # Gaussian elimination; field = None for Q, else prime p
    m = [list(r) + [b] for r, b in zip(rows, rhs)]
    ncol = len(rows[0]) if rows else 0
    def norm(x):
        return x % field if field else x
    m = [[norm(Fraction(x) if not field else x) for x in r] for r in m]
    r = 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(m)) if m[i][c] != 0), None)
        if piv is None: continue
        m[r], m[piv] = m[piv], m[r]
        inv = (pow(m[r][c], -1, field) if field else 1/m[r][c])
        m[r] = [norm(x*inv) for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [norm(a - f*b) for a, b in zip(m[i], m[r])]
        r += 1
    return all(any(x != 0 for x in row[:-1]) or row[-1] == 0 for row in m)

count_obj = 0; count_with_W = 0; bad = []
for n in range(3, NMAX+1):
    triples = list(itertools.combinations(range(n), 3))
    emax = (2*n - 1)//3
    for k in range(0, emax+1):
        for E in itertools.combinations(triples, k):
            if not is_object(n, E): continue
            count_obj += 1
            Wmaps = [e for e in E if strictly_closed(n, E, e)]
            if not Wmaps: continue
            count_with_W += 1
            # equations: sum t = 1; for each point p: s1(p)-s2(p)=0, s1(p)-s3(p)=0
            rows = [[1]*len(Wmaps)]; rhs = [1]
            for p in range(n):
                s = [[1 if e[i] == p else 0 for e in Wmaps] for i in range(3)]
                rows.append([a-b for a, b in zip(s[0], s[1])]); rhs.append(0)
                rows.append([a-b for a, b in zip(s[0], s[2])]); rhs.append(0)
            for field in (None, 2, 3, 5):
                if solvable(rows, rhs, field):
                    bad.append((n, E, field))
print("NMAX", NMAX, "objects", count_obj, "objects receiving an arrow from W", count_with_W)
print("targets with an affine equalizer (would refute A.1/A.3):", bad[:10], "count", len(bad))
