//Find the sum of the following series up to nth position / Print the following series up to
//nth position.
//○ 1^2 + 2^2 + 3^2 + ⋯
// Created by Sifat Ali on 1/12/2024.
//
#include <iostream>
using namespace std;

int sumOfseries(int arr[],int n){
    if(n==0) return arr[0]*arr[0];
    else return arr[n]*arr[n]+sumOfseries(arr,n-1);
}

int main(){
    int arr[]={1,2,3,4};
    int n = size(arr);

    cout<<sumOfseries(arr,n-1);
}