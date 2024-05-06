//Ballman Ford
// Created by hp on 4/16/2024.
//
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Graph {
public:
    int vertices;
    struct Edge {
        int src;
        int dest;
        int weight;
    };
    vector<Edge> adjList;//adg list

    Graph(int vertices) {
        this->vertices = vertices;
    }

    void addEdge(int src, int dest, int weight) {
        adjList.push_back({src, dest, weight});
    }

    void BellmanFord(int start) {
        vector<int> distance(vertices, INT_MAX); // Initialize distances to infinity
        vector<int> parent(vertices, -1); // Store parent vertices for the shortest path
        distance[start] = 0;

        // Relax all edges V-1 times
        for (int i = 0; i < vertices - 1; ++i) {
            for (auto edge : adjList) {
                if (distance[edge.src] != INT_MAX && distance[edge.src] + edge.weight < distance[edge.dest]) {
                    distance[edge.dest] = distance[edge.src] + edge.weight;
                    parent[edge.dest] = edge.src; // Update parent vertex
                }
            }
        }

        // Check for negative cycles
        for (auto edge : adjList) {
            if (distance[edge.src] != INT_MAX && distance[edge.src] + edge.weight < distance[edge.dest]) {
                cout << "Graph contains negative cycle!" << endl;
                return;
            }
        }

        // Print shortest paths
        for (int i = 0; i < vertices; ++i) {
            if (distance[i] != INT_MAX) {
                cout << "Shortest Path from vertex " << start << " to " << i << ": ";
                printPath(parent, i);
                cout << " (Total Weight: " << distance[i] << ")" << endl;
            } else {
                cout << "No path from vertex " << start << " to " << i << endl;
            }
        }
    }

    void printPath(vector<int> parent, int vertex) {
        stack<int> path;
        int current = vertex;
        while (current != -1) {
            path.push(current);
            current = parent[current];
        }
        while (!path.empty()) {
            cout << path.top() << " ";
            path.pop();
        }
    }
};

int main() {
    int V = 5;
    Graph g(V);

    g.addEdge(0, 1, -1);
    g.addEdge(0, 2, 4);
    g.addEdge(1, 2, 3);
    g.addEdge(1, 3, 2);
    g.addEdge(1, 4, 2);
    g.addEdge(3, 2, 5);
    g.addEdge(3, 1, 1);
    g.addEdge(4, 3, -3);


    g.BellmanFord(0);

    return 0;
}