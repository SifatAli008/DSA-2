//Merge Sort
// Created by Sifat Ali on 1/12/2024.
//
#include <iostream>
using namespace std;

void merge(int arr[], int start, int mid, int end) {
    int leftarr_size = mid - start + 1;
    int rightarr_size = end - mid;

    int leftarr[leftarr_size];
    for (int ind = 0; ind < leftarr_size; ind++) {
        leftarr[ind] = arr[start + ind];
    }

    int rightarr[rightarr_size];
    for (int ind = 0; ind < rightarr_size; ind++) {
        rightarr[ind] = arr[mid + 1 + ind];
    }

    int leftind = 0;
    int rightind = 0;

    for (int ind = start; ind <= end; ind++) {
        if (leftind == leftarr_size) {
            arr[ind] = rightarr[rightind];
            rightind++;
        } else if (rightind == rightarr_size) {
            arr[ind] = leftarr[leftind];
            leftind++;
        } else if (leftarr[leftind] < rightarr[rightind]) {
            arr[ind] = leftarr[leftind];
            leftind++;
        } else {
            arr[ind] = rightarr[rightind];
            rightind++;
        }
    }
}

void mergeSort(int arr[], int start, int end) {
   if(start==end){
       return;
   }

   else if (start < end) {
        int mid = start + (end - start) / 2;

        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);

        merge(arr, start, mid, end);
    }
}

int main() {
    int arr[] = {14, 7, 3, 12, 9, 11, 6, 2};
    int n = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, 0, n - 1);

    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }

    return 0;
}
