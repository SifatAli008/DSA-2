//Print array
// Created by Sifat Ali on 1/7/2024.
//
#include <iostream>
using namespace std;


void combination(int arr[],int n){
    if(n==0){
        return;
    }
    else{
        combination(arr,n-1);
        cout<<arr[n-1]<<" ";
    }
}

int main(){
    int arr[]={1,2,3,4,5};
    int n =size(arr);
    combination(arr,n);
}