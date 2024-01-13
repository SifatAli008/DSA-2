//Quick Sort
// Created by Sifat Ali on 1/12/2024.
//
#include <iostream>
using namespace std;

void swap(int &a,int &b){
    int temp=a;
    a=b;
    b=temp;
}

int Partiiton(int arr[],int start,int end){
   int pivot=arr[end];
   int i = start-1;

    for (int j = start; j <= end-1; ++j) {
        if(arr[j]<=pivot){
            i++;
            swap(arr[i],arr[j]);
        }
    }
    i++;
    swap(arr[i],arr[end]);
    return i;
}


void Quicksort(int arr[],int start, int end){
   if(start<end){
       int mid = Partiiton(arr,start,end);

       Quicksort(arr,start,mid-1);
       Quicksort(arr,mid+1,end);
   }
}

int main() {
    int arr[] = {9, -3, 5, 2, 6, 8, -6, 1,3};
    int n = sizeof(arr) / sizeof(arr[0]);

    Quicksort(arr, 0, n - 1);

    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }

    return 0;
}

