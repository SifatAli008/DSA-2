#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Disjoint_set {
    int *parent;
    int value;

public:
    Disjoint_set(int value) {
        this->value = value;
        parent = new int[value];
        for (int i = 0; i < value; i++) {
            parent[i] = i;
        }
    }

    ~Disjoint_set() {
        delete[] parent;
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }

    void union_sets(int x, int y) {
        int xroot = find(x);
        int yroot = find(y);
        parent[yroot] = xroot;
    }
};

// Structure to represent an edge
struct Edge {
    string src, dest;
    int weight;
};

// Comparator function to sort edges by weight
bool compareEdges(Edge a, Edge b) {
    return a.weight < b.weight;
}

// Function to find Minimum Spanning Tree using Kruskal's algorithm
vector<Edge> MST_Kruskal(vector<Edge> edges, int V, bool directed ) {
    vector<Edge> result;
    Disjoint_set ds(V);
    int totalWeight = 0; // Variable to store the total weight of the MST

    // Sort edges by weight
    sort(edges.begin(), edges.end(), compareEdges);

    // Iterate through all sorted edges
    for (auto edge : edges) {
        string src = edge.src;
        string dest = edge.dest;

        // Convert vertices to indices
        int x, y;
        if (src >= "a" && src <= "z") {
            x = src[0] - 'a';
        } else {
            x = src[0] - 'A';
        }
        if (dest >= "a" && dest <= "z") {
            y = dest[0] - 'a';
        } else {
            y = dest[0] - 'A';
        }

        // Find sets of source and destination vertices
        int xroot = ds.find(x);
        int yroot = ds.find(y);

        // If including this edge does not cause a cycle, include it in result and union the sets
        if (xroot != yroot) {
            result.push_back(edge);
            ds.union_sets(xroot, yroot);
            totalWeight += edge.weight; // Increment the total weight

            // If the graph is undirected, we add the reverse edge as well
            if (!directed) {
                result.push_back({dest, src, edge.weight});
                totalWeight += edge.weight; // Increment the total weight for the reverse edge
            }
        }
    }

    cout << "Total weight of the Minimum Spanning Tree: " << totalWeight << endl;

    return result;
}

int main() {
    // Example usage for undirected graph
    int V = 7; // Number of vertices

    vector<Edge> edges = {{"a", "b", 2},
                          {"a", "d", 8},
                          {"a", "e", 14},
                          {"b", "c", 19},
                          {"b", "e", 25},
                          {"c", "e", 17},
                          {"c", "f", 5},
                          {"c", "g", 9},
                          {"d", "e", 21},
                          {"e", "f", 2},
                          {"g", "f", 1}};

    vector<Edge> MST = MST_Kruskal(edges, V, false);

    // Output the edges of MST
    cout << "Edges in the Minimum Spanning Tree (Undirected Graph):\n";
    for (auto edge : MST) {
        cout << edge.src << " - " << edge.dest << " : " << edge.weight << endl;
    }

    return 0;
}
