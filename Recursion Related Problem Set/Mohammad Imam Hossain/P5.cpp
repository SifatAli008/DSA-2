//
// Created by Sifat Ali on 1/7/2024.
//
#include <iostream>
using namespace std;

void revers(int arr[],int n){
  if(n==1){
      cout<<arr[0];
  }else{
      cout<<arr[n-1]<<" ";
      revers(arr,n-1);
  }
}

int main(){
  int arr[]={10,20,5,2,3,5};
  int n= size(arr);
    revers(arr,n);
}