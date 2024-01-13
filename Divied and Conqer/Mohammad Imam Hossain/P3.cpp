//Binary search-MID
// Created by Sifat Ali on 1/12/2024.
//
#include <iostream>
using namespace std;

bool bin_search(int arr[],int startInd,int endInd,int search){

    if(startInd>endInd) return false;

    else{
        int mid=(startInd+endInd)/2;

        if(arr[mid]==search) return true;
        else if(search>arr[mid]) return bin_search(arr,mid +1,endInd,search);
        else return bin_search(arr,startInd,mid -1,search);

    }
}

int main(){
    int arr[]={2,5,9,50,100,150,200};
     int n=size(arr);

     int search;
     cout<<"Enter a search value : ";
     cin>>search;

     bool result = bin_search(arr,0,n-1,search);

     if(result) cout<<"Found";
      else  cout<<"Not Found";
    return 0;
}