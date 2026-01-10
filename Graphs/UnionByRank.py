"""
Disjoint Set: Union by Rank

Disjoint Set is any two arbitary nodes u & v belongs to same components or not.
Functionalities:
- Find the parent node
- Union: Rank/Size

Main Purpose: Join the smaller ranks to larger ranks.

Requirments
- Rank array, parent array

## Path Compression
Optimizing the edges by find the node's ultimate parent.
But the rank remains unchanged.
"""

# Python program for Union by Rank with Path Compression

class UnionFind:
    def __init__(self, n):
        self.Parent = list(range(n))  # Each node is its own parent
        self.Rank = [0] * n           # All ranks initialized to 0

    # Find with path compression
    def find(self, i):
        if self.Parent[i] != i:
            self.Parent[i] = self.find(self.Parent[i])
        return self.Parent[i]

    # Union by rank
    def unionByRank(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)

        if irep == jrep:
            return

        # Attach smaller rank tree under larger rank root
        if self.Rank[irep] < self.Rank[jrep]:
            self.Parent[irep] = jrep
        elif self.Rank[irep] > self.Rank[jrep]:
            self.Parent[jrep] = irep
        else:
            self.Parent[jrep] = irep
            self.Rank[irep] += 1

if __name__ == "__main__":
    n = 5
    unionFind = UnionFind(n)
    unionFind.unionByRank(0, 1)
    unionFind.unionByRank(2, 3)
    unionFind.unionByRank(0, 4)

    # Print representatives
    # Path compression
    for i in range(n):
        print(f'Element {i}: Representative = {unionFind.find(i)}')
