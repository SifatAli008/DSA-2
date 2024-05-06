//
// Created by Sifat Ali on 4/6/2024.
//
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int isNegativeWeightCycle(int n, vector<vector<int>>& edges) {
    vector<int> dist(n, INT_MAX);
    dist[0] = 0;

    // Relax edges repeatedly
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < edges.size(); j++) {
            int src = edges[j][0];
            int dest = edges[j][1];
            int weight = edges[j][2];

            if (dist[src] != INT_MAX && dist[src] + weight < dist[dest]) {
                dist[dest] = dist[src] + weight;
            }
        }
    }

    // Check for negative weight cycles
    for (int j = 0; j < edges.size(); j++) {
        int src = edges[j][0];
        int dest = edges[j][1];
        int weight = edges[j][2];

        if (dist[src] != INT_MAX && dist[src] + weight < dist[dest]) {
            return 1; // Negative weight cycle detected
        }
    }

    return 0; // No negative weight cycle detected
}

int main() {
    int n = 5; // Number of vertices
    vector<vector<int>> edges = {{0, 1, -1}, {0, 2, 4}, {1, 2, 3}, {1, 3, 2}, {1, 4, 2}, {3, 2, 5}, {3, 1, 1}, {4, 3, -3}}; // Example edges
    cout << isNegativeWeightCycle(n, edges) << endl; // Output: 1 (Negative weight cycle detected)

    return 0;
}
