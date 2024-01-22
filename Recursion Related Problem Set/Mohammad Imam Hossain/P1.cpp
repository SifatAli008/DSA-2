//MAX
// Created by Sifat Ali on 1/7/2024.
//
#include <iostream>
using namespace std;

int recursion(int arr[],int n){
    if(n==1){//base case
        return arr[0];
    }
    else{//recarsive case
        int i=arr[n-1];//check small part
        int result=recursion(arr,n-1);
        if(i>result){
            return i;
        }
        else{
            return result;
        }
    }
}



int main(){
 int arr[]={1,2,3,10,5,6,9};
   int lenght =size(arr);
  cout<<recursion(arr,lenght);
}
