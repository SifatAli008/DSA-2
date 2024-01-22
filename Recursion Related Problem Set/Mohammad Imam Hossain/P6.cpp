//
// Created by Sifat Ali on 1/7/2024.
//
#include <iostream>
using namespace std;

int min(int arr[],int n){
    if(n==1){
        return arr[0];
    } else{
        int i=arr[n-1];
        int result= min(arr,n-1);
        if(i<result){
            return i;
        } else{
            return result;
        }
    }
}

int main(){
  int arr[]={10,23,9,3,30,1,39,55,4,33};
  int n=size(arr);
  cout<<min(arr,n);

}
