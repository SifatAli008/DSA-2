//tower of hanio
// Created by Sifat Ali on 1/10/2024.
//
#include <iostream>
#include <stack>
using namespace std;

struct HanoiParameters {
    int n, i, j, k;
};

int countMoves(int n) {
    if (n <= 0) return 0;
    return (2 * countMoves(n - 1)) + 1;
}

void Hanoi(int n, int i, int j, int k) {
    stack<HanoiParameters> hanoiStack;
    hanoiStack.push({n, i, j, k});
    int moves = 0;

    while (!hanoiStack.empty()) {
        HanoiParameters params = hanoiStack.top();
        hanoiStack.pop();

        if (params.n == 1) {
            cout << "Move disk from " << params.i << " to " << params.k << endl;
            moves++;
        } else {
            HanoiParameters params1 = {params.n - 1, params.j, params.i, params.k};
            HanoiParameters params2 = {1, params.i, params.j, params.k};
            HanoiParameters params3 = {params.n - 1, params.i, params.k, params.j};

            hanoiStack.push(params3);
            hanoiStack.push(params2);
            hanoiStack.push(params1);
        }
    }

}

int main() {
    int n = 3;
    int i = 1, j = 2, k = 3;
    Hanoi(n, i, j, k);

    int totalMoves = countMoves(n);
    cout << "Total moves  " << totalMoves << endl;

    return 0;
}
