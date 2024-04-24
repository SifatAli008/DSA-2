//MST_Kruskal -0,1
// Created by Sifat Ali on 5/4/2024.
//
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Disjoint_set {
    int *parent;
    int *rank;
    int value;

public:
    Disjoint_set(int value) {
        this->value = value;
        parent = new int[value];
        rank = new int[value];
        for (int i = 0; i < value; i++) {
            parent[i] = i;
            rank[i] = 0; // Initialize rank of each set to 0
        }
    }

    Disjoint_set() {
        delete[] parent;
        delete[] rank;
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void union_sets(int x, int y) {
        int xroot = find(x);
        int yroot = find(y);

        if (xroot == yroot) return; // Already in the same set

        if (rank[xroot] < rank[yroot]) {
            parent[xroot] = yroot;
        } else if (rank[xroot] > rank[yroot]) {
            parent[yroot] = xroot;
        } else {
            parent[yroot] = xroot;
            rank[xroot]++;
        }
    }
};

// Structure to represent an edge
struct Edge {
    int src, dest;
    int weight;
};

// Comparator function to sort edges by weight
bool compareEdges(Edge a, Edge b) {
    return a.weight < b.weight;
}

// Function to find Minimum Spanning Tree using Kruskal's algorithm
vector<Edge> MST_Kruskal(vector<Edge> edges, int V) {
    vector<Edge> result;
    Disjoint_set ds(V);
    int totalWeight = 0; // Variable to store the total weight of the MST

    // Sort edges by weight
    sort(edges.begin(), edges.end(), compareEdges);

    // Iterate through all sorted edges
    for (auto& edge : edges) {
        int src = edge.src;
        int dest = edge.dest;

        // Find sets of source and destination vertices
        int x = ds.find(src);
        int y = ds.find(dest);

        // If including this edge does not cause a cycle, include it in result and union the sets
        if (x != y) {
            result.push_back(edge);
            ds.union_sets(x, y);
            totalWeight += edge.weight; // Increment the total weight
        }
    }

    cout << "Total weight of the Minimum Spanning Tree: " << totalWeight << endl;

    return result;
}

int main() {
    // Example usage for undirected graph
    int V = 9; // Number of vertices

    vector<Edge> edges = {{0, 1, 4},
                          {0, 7, 8},
                          {1, 2, 8},
                          {1, 7, 11},
                          {2, 3, 7},
                          {2, 5, 4},
                          {2, 8, 2},
                          {3, 4, 9},
                          {3, 5, 14},
                          {4, 5, 10},
                          {5, 6, 2},
                          {6, 7, 1},
                          {6, 8, 6},
                          {7, 8, 1}};

    vector<Edge> MST = MST_Kruskal(edges, V);

    // Output the edges of MST
    cout << "Edges in the Minimum Spanning Tree (Undirected Graph):\n";
    for (auto& edge : MST) {
        cout << edge.src << " - " << edge.dest << " : " << edge.weight << endl;
    }

    return 0;
}
