//11. Find the largest and smallest element of a given array.
// Created by Sifat Ali on 1/8/2024.
//

#include <iostream>
using namespace std;

int max(int arr[],int n){
    if(n==1){
        return arr[0];
    } else{
        int i=arr[n-1];//check small part
        int result=max(arr,n-1);
        if(i>result){
            return i;
        }
        else{
            return result;
        }
    }
}

int min(int arr[],int n){
    if(n==1){
        return arr[0];
    } else{
        int i=arr[n-1];//check small part
        int result=min(arr,n-1);
        if(i<result){
            return i;
        }
        else{
            return result;
        }
    }
}



int main(){
    int arr[]={10,20,5,2,3,5};
    int n= size(arr);

    cout<<"Max : "<<max(arr,n-1)<<endl;
    cout<<"Min : "<<min(arr,n-1);
}