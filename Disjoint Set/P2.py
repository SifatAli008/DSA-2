class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_sets(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[yroot] < self.rank[xroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

    def is_cyclic(self, x, y):
        return self.find(x) == self.find(y)


# Example usage
ds = DisjointSet(5)

ds.union_sets(0, 2)
ds.union_sets(1, 4)
ds.union_sets(3, 2)

print("Representative of 0:", ds.find(0))
print("Representative of 1:", ds.find(1))
print("Representative of 2:", ds.find(2))
print("Representative of 3:", ds.find(3))

print("Is there a cycle between 3 and 4:", ds.is_cyclic(3, 4))
print("Is there a cycle between 1 and 4:", ds.is_cyclic(1, 4))
