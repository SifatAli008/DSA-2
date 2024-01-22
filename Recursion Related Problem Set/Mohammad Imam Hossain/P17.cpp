//tower of hanio
// Created by Sifat Ali on 1/10/2024.
//
#include <iostream>
#include <stack>
using namespace std;

void Hanoi(int n, int i, int j, int k) {
    stack<int> stackN, stackI, stackJ, stackK;

    stackN.push(n);
    stackI.push(i);
    stackJ.push(j);
    stackK.push(k);

    while (!stackN.empty()) {
        n = stackN.top();
        i = stackI.top();
        j = stackJ.top();
        k = stackK.top();

        stackN.pop();
        stackI.pop();
        stackJ.pop();
        stackK.pop();

        if (n == 1) {
            cout << "Move disk from " << i << " to " << k << endl;
        } else {
            stackN.push(n - 1);
            stackI.push(j);
            stackJ.push(i);
            stackK.push(k);

            stackN.push(1);
            stackI.push(i);
            stackJ.push(j);
            stackK.push(k);

            stackN.push(n - 1);
            stackI.push(i);
            stackJ.push(k);
            stackK.push(j);
        }
    }
}

int main() {
    int n = 3;  // Number of disks
    int source = 1, auxiliary = 2, destination = 3;

    Hanoi(n, source, auxiliary, destination);

    return 0;
}
