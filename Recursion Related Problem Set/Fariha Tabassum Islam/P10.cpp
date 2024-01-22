//10. Write a recursive program to find the maximum of the elements of an array of size n.
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;

int max(int arr[],int size){
    if(size==0)return arr[0];
    else{
        int m=arr[size];
        int remain = max(arr,size-1);
        if(m>remain){
            return m;
        } else{
            return remain;
        }
    }
}

int main(){
    int arr[]={30,1,4,99,0,28};
    int n= size(arr);
    cout<<max(arr,n);
}