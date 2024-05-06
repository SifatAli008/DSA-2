#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <climits>

using namespace std;

typedef pair<int, int> Pair;

// Define the graph as an adjacency list
map<char, vector<Pair>> graph;

// Function to run Dijkstra's algorithm from the source node
map<char, int> dijkstra(char source) {
    // Initialize distance dictionary with infinity for all nodes
    map<char, int> distance;
    for (const auto &entry : graph) {
        distance[entry.first] = INT_MAX;
    }
    // Set the source node's distance to 0
    distance[source] = 0;

    // Initialize the priority queue
    priority_queue<Pair, vector<Pair>, greater<Pair>> pq;
    pq.push({0, source});

    while (!pq.empty()) {
        // Get the node with the shortest distance
        char current_node = pq.top().second;
        int current_distance = pq.top().first;
        pq.pop();

        // Explore each neighbor of the current node
        for (const auto &neighbor : graph[current_node]) {
            char neighbor_node = neighbor.first;
            int weight = neighbor.second;

            int tentative_distance = current_distance + weight;

            // If a shorter path is found, update the distance
            if (tentative_distance < distance[neighbor_node]) {
                distance[neighbor_node] = tentative_distance;
                // Add the neighbor to the priority queue with the updated distance
                pq.push({tentative_distance, neighbor_node});
            }
        }
    }

    return distance;
}

int main() {
    // Define a graph as an adjacency list
    graph = {
            {'A', {{'B', 1}, {'C', 4}}},
            {'B', {{'A', 1}, {'C', 2}, {'D', 5}}},
            {'C', {{'A', 4}, {'B', 2}, {'D', 1}}},
            {'D', {{'B', 5}, {'C', 1}}}
    };

    // Run Dijkstra's algorithm from source node 'A'
    char source_node = 'A';
    map<char, int> distances = dijkstra(source_node);

    // Print the distances from the source node to other nodes
    for (const auto &entry : distances) {
        cout << "Distance from " << source_node << " to " << entry.first << ": " << entry.second << endl;
    }

    return 0;
}
