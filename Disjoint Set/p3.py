import heapq

def calculate_prims_mst(n, edges):
    # Create adjacency list
    adj = {i: [] for i in range(1, n+1)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    key = [float('inf')] * (n + 1)
    mst = [False] * (n + 1)
    parent = [-1] * (n + 1)

    # Start the algorithm
    key[1] = 0
    parent[1] = -1
    pq = [(0, 1)]
    while pq:
        _, u = heapq.heappop(pq)
        mst[u] = True
        for v, w in adj[u]:
            if not mst[v] and w < key[v]:
                parent[v] = u
                key[v] = w
                heapq.heappush(pq, (w, v))

    result = []
    for i in range(2, n + 1):
        result.append(((parent[i], i), key[i]))
    return result

def main():
    n = 5  # Number of vertices
    edges = [
        (1, 2, 2),
        (1, 3, 3),
        (2, 3, 1),
        (2, 4, 4),
        (3, 4, 5),
        (3, 5, 7),
        (4, 5, 6)
    ]

    mst = calculate_prims_mst(n, edges)

    print("Edges in MST:")
    for edge in mst:
        print(f"{edge[0][0]} - {edge[0][1]} : {edge[1]}")


main()
