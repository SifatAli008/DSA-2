//Print the array elements.
// Created by Sifat Ali on 1/8/2024.
//

#include <iostream>
using namespace std;

void PrintArray(int arr[],int n){
    if(n==0){
        return;
    }else{
        PrintArray(arr,n-1);
        cout<<arr[n-1]<<" ";
    }
}

int main(){
    int arr[]={10,20,5,2,3,5};
    int n= size(arr);
    PrintArray(arr,n);
}