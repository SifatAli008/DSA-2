//Write a recursive program to count the prime numbers of an array of n integers
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;

bool isPrime(int num, int i) {
    if (i <= 1) {
        return true;
    } else {
        if (num % i == 0) {
            return false;
        } else {
            return isPrime(num, i - 1);
        }
    }
}

int countPrimes(int arr[], int n, int i) {
    if (n < 0) {
        return 0;
    } else {
        if (isPrime(arr[n], arr[n] - 1)) {
            return 1 + countPrimes(arr, n - 1, i);
        } else {
            return countPrimes(arr, n - 1, i);
        }
    }
}

int main() {
    int arr[] = {12, 5, 7, 15, 2, 21};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Prime numbers count: " << countPrimes(arr, n - 1, 2) << endl;

    return 0;
}
