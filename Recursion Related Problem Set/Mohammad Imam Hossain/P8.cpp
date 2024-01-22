//sum of array
// Created by Sifat Ali on 1/7/2024.
//
#include <iostream>
using namespace std;

int sum=0;

void sumOfArray(int arr[],int n){
    if(n==0){
        return ;
    } else{
      sumOfArray(arr,n-1);
     sum+=arr[n-1];
    }
}


int main(){
 int arr[]={1,2,3,4,5};
   int n=size(arr);
    sumOfArray(arr,n);
    cout<<sum;
}