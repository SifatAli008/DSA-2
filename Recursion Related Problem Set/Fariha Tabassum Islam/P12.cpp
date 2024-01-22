//12. Write a recursive program to find the average of the elements of an array of size n
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;
double sum(int arr[], int n) {
    if (n == 0) {
        return 0;
    } else {
        return arr[n - 1] + sum(arr, n - 1);
    }
}

double avg(int arr[], int n) {
    if (n == 0) {
        return 0;
    } else {
        return sum(arr, n) / n;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    double result = avg(arr, n);
    cout << result << endl;

    return 0;
}
