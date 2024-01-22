//17. Write a recursive program to find the maximum of a 2d array.
// Created by Sifat Ali on 1/12/2024.
//
#include <iostream>
using namespace std;

const int ROWS = 3; // Assuming a 3x3 array for this example
const int COLS = 3;

int max(int arr[ROWS][COLS], int row, int col) {
    if (row == 0 && col == 0) {
        return arr[0][0];
    } else {
        int current = arr[row][col];
        int maxInRemaining = 0;

        if (col > 0) {
            maxInRemaining = max(arr, row, col - 1);
        } else if (row > 0) {
            maxInRemaining = max(arr, row - 1, COLS);
        }

        return max(current, maxInRemaining);
    }
}

int main() {
    int arr[ROWS][COLS] = {
            {2, 55, 10},
            {0, 40, 2},
            {40, -2, 3}
    };

    int m = max(arr, ROWS - 1, COLS - 1);

    cout << "Maximum element in the 2D array: " << m << endl;

    return 0;
}
