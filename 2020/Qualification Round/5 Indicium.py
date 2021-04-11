# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209aa0

from __future__ import print_function
INF = float("inf")
input = raw_input
range = xrange

ans = [[]]

class Dinic:
    def __init__(self, n):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, a, b, c, rcap=0):
        self.adj[a].append([b, len(self.adj[b]), c, 0])
        self.adj[b].append([a, len(self.adj[a]) - 1, rcap, 0])

    def dfs(self, v, t, f):
        if v == t or not f:
            return f

        for i in range(self.ptr[v], len(self.adj[v])):
            e = self.adj[v][i]
            if self.lvl[e[0]] == self.lvl[v] + 1:
                p = self.dfs(e[0], t, min(f, e[2] - e[3]))
                if p:
                    self.adj[v][i][3] += p
                    self.adj[e[0]][e[1]][3] -= p
                    return p
            self.ptr[v] += 1

        return 0

    def calc(self, s, t):
        flow, self.q[0] = 0, s
        for l in range(31):  # l = 30 maybe faster for random data
            while True:
                self.lvl, self.ptr = [0] * len(self.q), [0] * len(self.q)
                qi, qe, self.lvl[s] = 0, 1, 1
                while qi < qe and not self.lvl[t]:
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
                            self.q[qe] = e[0]
                            qe += 1
                            self.lvl[e[0]] = self.lvl[v] + 1

                p = self.dfs(s, t, INF)
                while p:
                    flow += p
                    p = self.dfs(s, t, INF)

                if not self.lvl[t]:
                    break

        return flow

def fill(x, n):
    mf = Dinic(2*n + 2)
    global ans
    for i in range(n):
        for j in range(n):
            if ans[i][j] == 0:
                mf.add_edge(i, j + n, 1)
        mf.add_edge(2*n, i, 1)
        mf.add_edge(i + n, 2*n + 1, 1)
    mf.calc(2*n, 2*n + 1)
    for i in range(n):
        for e in mf.adj[i]:
            if (e[0] < n or e[0] >= 2*n):
                continue
            if e[3] == 1:
                ans[i][e[0] - n] = x
                break

def solve():
    n, k = map(int, input().split())
    #print('{} {}'.format(n, k))
    bad = [[3, 5], [3, 7]]
    possible = True
    if k == n + 1 or k == n*n - 1 or [n, k] in bad:
        print("IMPOSSIBLE")
        return
    print("POSSIBLE")
    global ans
    ans = [[0 for x in range(n)] for x in range(n)]
    idx = list(range(1, n + 1))
    avg = k//n
    rem = k%n
    if rem == 0:
        idx.remove(avg)
        for i in range(n):
            ans[i][i] = avg
    elif rem == 1:
        idx.remove(avg)
        idx.remove(avg - 1)
        idx.remove(avg + 1)
        for i in range(n - 3):
            ans[i][i] = avg
            ans[i + 1][i] = avg - 1
            if i > 0:
                ans[i - 1][i] = avg + 1
        ans[n - 2][n - 3] = ans[n - 1][n - 1] = ans[0][n - 2] = avg - 1
        ans[n - 1][0] = ans[n - 4][n - 1] = ans[n - 2][n - 2] = ans[n - 3][n - 3] = avg + 1
        ans[n - 1][n - 3] = ans[n - 3][n - 2] = ans[n - 2][n - 1] = avg
    elif rem == n - 1:
        avg += 1
        idx.remove(avg)
        idx.remove(avg - 1)
        idx.remove(avg + 1)
        for i in range(n - 3):
            ans[i][i] = avg
            ans[i + 1][i] = avg + 1
            if i > 0:
                ans[i - 1][i] = avg - 1
        ans[n - 2][n - 3] = ans[n - 1][n - 1] = ans[0][n - 2] = avg + 1
        ans[n - 1][0] = ans[n - 4][n - 1] = ans[n - 2][n - 2] = ans[n - 3][n - 3] = avg - 1
        ans[n - 1][n - 3] = ans[n - 3][n - 2] = ans[n - 2][n - 1] = avg
    else:
        idx.remove(avg)
        idx.remove(avg + 1)
        for i in range(n):
            ans[i][i] = avg + 1 if i < rem else avg
            if i < rem - 1:
                ans[i + 1][i] = avg
            if i > rem:
                ans[i - 1][i] = avg + 1
        ans[n - 1][rem] = avg + 1
        ans[0][rem - 1] = avg

    for val in idx:
        fill(val, n)

    for v in ans:
        print(' '.join(str(x) for x in v))

def main():
    t = int(input())
    for i in range(t):
        print("Case #{}: ".format(i + 1), end = '')
        solve()

if __name__ == '__main__':
    main()