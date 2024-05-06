class DisjointSet:
    def __init__(self, value):
        self.parent = list(range(value))
        self.value = value

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union_sets(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        self.parent[yroot] = xroot

    def cycle(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        result = (xroot == yroot)
        print("true" if result else "false")
        return result


if __name__ == "__main__":
    ds = DisjointSet(5)

    ds.union_sets(0, 2)
    ds.union_sets(1, 4)
    ds.union_sets(3, 2)

    print("Representative of 0:", ds.find(0))
    print("Representative of 1:", ds.find(1))
    print("Representative of 2:", ds.find(2))
    print("Representative of 3:", ds.find(3))

    print("cycle(3, 4): ", end="")
    ds.cycle(3, 4)
    print("cycle(1, 4): ", end="")
    ds.cycle(1, 4)
