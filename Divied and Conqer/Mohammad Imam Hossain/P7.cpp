//count inversion
// Created by Sifat Ali on 1/12/2024.
//
#include <iostream>
using namespace std;

int count(int arr[], int start, int mid, int end) {
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

    int invcounter=0;
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
        } else {//left>right
            arr[ind] = rightarr[rightind];
            rightind++;

            invcounter+=(leftarr_size-leftind);
        }
    }
    return invcounter;
}

int countInversion(int arr[], int start, int end) {
    if (start>end){
        return 0;
    }

    if(start==end){
        return 0;
    }

    else if (start < end) {
        int mid = start + (end - start) / 2;

    int firsthalf = countInversion(arr, start, mid);
    int secondhalf =  countInversion(arr, mid + 1, end);

    int total = count(arr, start, mid, end);

        return total+firsthalf+secondhalf;
    }
}

int main() {
    int arr[] = {8,  3, 5 ,1};
    int n = sizeof(arr) / sizeof(arr[0]);

  cout<<"Inversount count:" <<countInversion(arr, 0, n - 1);



    return 0;
}
