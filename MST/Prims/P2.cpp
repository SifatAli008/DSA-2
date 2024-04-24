// Prims
// Created by Sifat Ali on 4/5/2024.
//
#include <iostream>
#include <vector>
#include <climits>

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

    // Function to find Minimum Spanning Tree using Prim's algorithm
    vector<Edge> MST_Prim(int startVertex) {
        vector<Edge> result;
        vector<bool> inMST(vertices, false); // To track vertices included in MST
        vector<int> minWeight(vertices, INT_MAX); // To store minimum weight
        vector<int> parent(vertices, -1); // To store parent of each vertex in MST

        // Start from the given startVertex
        minWeight[startVertex] = 0;

        // Iterate vertices-1 times to add vertices-1 edges to MST
        for (int i = 0; i < vertices - 1; ++i) {
            // Find vertex with minimum weight edge that is not yet in MST
            int minVertex = -1;
            for (int v = 0; v < vertices; ++v) {
                if (!inMST[v] && (minVertex == -1 || minWeight[v] < minWeight[minVertex])) {
                    minVertex = v;
                }
            }

            // Add the minimum weight edge to MST
            if (minVertex != -1) {
                inMST[minVertex] = true;

                // Add the edge to result
                if (parent[minVertex] != -1) {
                    result.push_back({parent[minVertex], minVertex, minWeight[minVertex]});
                }

                // Update minWeight and parent for adjacent vertices
                for (Edge edge : adjList) {
                    if (edge.src == minVertex) {
                        int v = edge.dest;
                        int weight = edge.weight;
                        if (!inMST[v] && weight < minWeight[v]) {
                            minWeight[v] = weight;
                            parent[v] = minVertex;
                        }
                    }
                    else if (edge.dest == minVertex) {
                        int v = edge.src;
                        int weight = edge.weight;
                        if (!inMST[v] && weight < minWeight[v]) {
                            minWeight[v] = weight;
                            parent[v] = minVertex;
                        }
                    }
                }
            }
        }

        return result;
    }
};

int main() {
    int V = 7; // Number of vertices

    // Create a graph
    Graph graph(V);

    // Adding edges to the graph
    graph.addEdge(0, 1, 2);
    graph.addEdge(0, 3, 8);
    graph.addEdge(0, 4, 14);
    graph.addEdge(1, 2, 19);
    graph.addEdge(1, 4, 25);
    graph.addEdge(2, 4, 17);
    graph.addEdge(2, 5, 5);
    graph.addEdge(2, 6, 9);
    graph.addEdge(3, 4, 21);
    graph.addEdge(4, 5, 13);
    graph.addEdge(5, 6, 1);

    // Take starting vertex from the user
    int startVertex;
    cout << "Enter the starting vertex: ";
    cin >> startVertex;

    // Ensure the input is within bounds
    if (startVertex < 0 || startVertex >= V) {
        cout << "Invalid starting vertex!" << endl;
        return 1; // Exit with error
    }

    // Find MST with the provided starting vertex
    auto MST = graph.MST_Prim(startVertex);

    // Output the edges of MST
    cout << "Edges in the Minimum Spanning Tree (Undirected Graph):\n";
    int totalWeight = 0;
    for (auto edge : MST) {
        cout << edge.src << " - " << edge.dest << " : " << edge.weight << endl;
        totalWeight += edge.weight;
    }

    // Output the total weight of the MST
    cout << "Total weight of Minimum Spanning Tree: " << totalWeight << endl;

    return 0;
}