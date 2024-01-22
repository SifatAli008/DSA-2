//Frequency
// Created by Sifat Ali on 1/7/2024.
//
#include <iostream>
using namespace std;

int Frequency(int arr[],int size,int num){
       if(size==0){
           return 0;
       }else{
         if(arr[size]==num){
             return 1 + Frequency(arr, size - 1, num);
         }else{
             return Frequency(arr,size-1,num);
         }
       }
}

int main(){
    int arr[]={10,4,9,3,30,1,39,55,4,33};
    int n=size(arr);

     int num;
     cout<<"Enter the Number: ";
    cin>>num;
    cout<<Frequency(arr,n,num);

}