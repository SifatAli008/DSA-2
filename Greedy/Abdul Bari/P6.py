class Edge:
    def __init__(self, to, cost):  # Changed dis to cost
        self.to = to
        self.cost = cost  # Changed dis to cost

def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n):
        min_dist = float('inf')
        min_node = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_node = i
        if min_node == -1:
            break
        visited[min_node] = True
        
        for edge in graph[min_node]:
            to, cost = edge.to, edge.cost 
            if dist[min_node] + cost < dist[to]:
                dist[to] = dist[min_node] + cost

    return dist

def main():
    v = 4
    graph = [[] for _ in range(v)]

    graph[0].append(Edge(1, 10)) 

    graph[1].append(Edge(2, 12))  
    graph[1].append(Edge(3, 30))  

    graph[2].append(Edge(0, 59))  
    graph[2].append(Edge(1, 11))  
    graph[2].append(Edge(3, 22)) 

    graph[3].append(Edge(2, 7))  
    graph[3].append(Edge(1, 71)) 

    start_node = 1
    distances = dijkstra(graph, start_node)

    for i, distance in enumerate(distances):
        print(f"Distance from node {start_node} to node {i}: {distance}")


main()
