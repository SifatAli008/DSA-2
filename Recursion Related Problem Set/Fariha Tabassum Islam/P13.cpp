//13. Write a recursive program to print the odd/even numbers of an array of n integers
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;

void PrintEvenOdd(int arr[], int size,bool choice) {
    if (size < 0) {
        return;
    } else {
        if (arr[size] % 2 == 0 && choice) {
            PrintEvenOdd(arr, size - 1, choice);
            cout << arr[size] << " ";
        }  else if (arr[size] % 2 !=0 && !choice) {
            PrintEvenOdd(arr, size - 1, choice);
            cout << arr[size] << " ";
        } else {
            PrintEvenOdd(arr, size - 1, choice);
        }
    }
}

int main() {
    int arr[] = {1, 0, 3, 4, 5, 6, -1, 8 };
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Even numbers: ";
    PrintEvenOdd(arr, n - 1, true);
    cout << endl;

    cout << "Odd numbers: ";
    PrintEvenOdd(arr, n - 1, false);
    cout << endl;

    return 0;
}
