//Prims
// Created by Sifat Ali on 4/5/2024.
//
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// Structure to represent a graph edge
struct Edge {
    int source;
    int weight;
    Edge(int t, int w) {
        source = t;
        weight = w;
    }
};

// Function to find the minimum spanning tree using Prim's algorithm
void primMST(vector<vector<Edge>> graph, int r) {
    int V = graph.size();
    vector<int> key(V, INT_MAX); // Key values used to pick minimum weight edge
    vector<int> parent(V, -1); // Array to store constructed MST
    vector<bool> inMST(V, false); // To represent set of vertices included in MST

    key[r] = 0; // Make key 0 so that this vertex is picked as first vertex

    for (int count = 0; count < V - 1; ++count) {
        // Pick the minimum key vertex from the set of vertices not yet included in MST
        int u = -1;
        for (int v = 0; v < V; ++v) {
            if (!inMST[v] && (u == -1 || key[v] < key[u]))
                u = v;
        }

        inMST[u] = true; // Add the picked vertex to the MST

        // Update key and parent index of the adjacent vertices of the picked vertex
        for (Edge& e : graph[u]) {
            int v = e.source;
            int weight = e.weight;
            if (!inMST[v] && weight < key[v]) {
                parent[v] = u;
                key[v] = weight;
            }
        }
    }

    // Print the constructed MST
    cout << "Edge   Weight\n";
    for (int i = 0; i < V; ++i) {
        if (i != r)
            cout << parent[i] << " - " << i << "    " << key[i] << "\n";
    }
}

int main() {
    int V, E;
    cout << "Enter number of vertices and edges: ";
    cin >> V >> E;

    // Initialize graph as an adjacency list
    vector<vector<Edge>> graph(V);

    cout << "Enter edges (format: source destination weight):\n";
    for (int i = 0; i < E; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back(Edge(v, w));
        graph[v].push_back(Edge(u, w)); // Assuming undirected graph
    }

    int root;
    cout << "Enter the root vertex: ";
    cin >> root;

    // Find and print the minimum spanning tree using Prim's algorithm
    primMST(graph, root);

    return 0;
}
