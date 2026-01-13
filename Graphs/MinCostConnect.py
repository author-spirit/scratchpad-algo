"""
1584. Min Cost to Connect All Points

Ref: https://leetcode.com/problems/min-cost-to-connect-all-points/description/
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
n = 4
costs = []

# u -> [(v,wt)]
# (wt, u, v)
for i, u_point in enumerate(points):
    for j, v_point in enumerate(points):
        if i != j:
            # manhattan
            wt = abs(u_point[0] - v_point[0]) + abs(u_point[1] - v_point[1])
            costs.append((wt, i, j))

# print(costs)

uf = UnionFind(n)
mst_weight = 0

costs.sort(key=lambda x: x[0])

for w, u, v in costs:
    if uf.union(u, v):
        mst_weight += w

print(mst_weight)

print("costs", costs)
