//Find the sum of the following series up to nth position / Print the following series up to
//nth position.
//○ 2 ∗ 3 + 4 ∗ 5 + 8 ∗ 7 + 16 ∗ 9 + ⋯
// Created by Sifat Ali on 1/12/2024.
//
#include <iostream>
using namespace std;

int sumOfseries(int arr[], int n, int i) {
    if (n == 0) {
        return arr[0] * i;
    } else {
        return arr[n] * (i + 2 * n) + sumOfseries(arr, n - 1, i);
    }
}

int main() {
    int arr[] = {1, 2, 3, 4};
    int n = sizeof(arr) / sizeof(arr[0]); ;

    cout << "Sum of the series up to nth position: " << sumOfseries(arr, n - 1, 3) << endl;

    return 0;
}
