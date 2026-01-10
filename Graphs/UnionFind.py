"""
Disjoint Set where two set have no common values
Disjoint Set: Union by Rank
    - Find the parent node
    - Union: Rank


    Requirments
    - Rank array, parent array

Union By Size:
    Similar to Union by rank, here we retain the height of the graph.

Intuition: Join the smaller ranks/size to larger ranks/size.

## Path Compression
Optimizing the edges by find the node's ultimate parent.
But the rank remains unchanged.
"""

class UnionFind:
    def __init__(self, n):
        n +=1
        self.Parent = list(range(n))  # Each node is its own parent
        self.Rank = [0] * n          # All ranks initialized to 0
        self.Size = [1] * n           # all size initialized to 1

    # Find with path compression
    def find_par(self, i):
        if self.Parent[i] != i:
            self.Parent[i] = self.find_par(self.Parent[i])      # update the ith parent
        return self.Parent[i]

    # Union by rank
    def union_by_rank(self, u, v):
        ult_u = self.find_par(u)
        ult_v = self.find_par(v)

        if ult_u == ult_v:
            return

        # Attach smaller rank tree under larger rank root
        if self.Rank[ult_u] < self.Rank[ult_v]:
            self.Parent[ult_u] = ult_v
        elif self.Rank[ult_u] > self.Rank[ult_v]:
            self.Parent[ult_v] = ult_u
        else:
            self.Parent[ult_v] = ult_u
            self.Rank[ult_u] += 1

    # Union by size
    def union_by_size(self, u, v):
        ult_u = self.find_par(u)
        ult_v = self.find_par(v)

        if ult_u == ult_v:
            return

        # Update the parent based on the Size
        # Increment the Size of Ultimate Parent with the Size of u|v th ultimate parent
        if self.Size[ult_v] > self.Size[ult_u]:
            self.Parent[ult_u] = ult_v
            self.Size[ult_v] += self.Size[ult_u]
        else:
            # prefernece to u
            self.Parent[ult_v] = ult_u
            self.Size[ult_u] += self.Size[ult_v]


if __name__ == "__main__":
    n = 7
    graphs = [(1,2), (2,3), (4,5), (6,7), (5,6), (3,7)]
    unionFind = UnionFind(n)

    # Union By Rank
    print("Union By Rank")
    for nodes in graphs:
        unionFind.union_by_rank(*nodes)

    print(unionFind.Parent)

    # Union By Rank
    print("=================================")
    print("Union By Size")
    unionFind = UnionFind(n)
    unionFind.union_by_size(1,2)
    unionFind.union_by_size(2,3)
    unionFind.union_by_size(4,5)
    unionFind.union_by_size(6,7)
    unionFind.union_by_size(5,6)
    unionFind.union_by_size(3,7)

    print("same" if unionFind.find_par(3) == unionFind.find_par(7) else "not same")

    print(unionFind.Parent)
