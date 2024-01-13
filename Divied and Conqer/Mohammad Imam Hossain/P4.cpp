//Binary search-random
// Created by Sifat Ali on 1/12/2024.
//
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int random_ind(int s,int e){
    srand(time(nullptr));//seed per sec
    int randint=s+rand()%(e-s+1);//s+01
    return randint;
}


bool bin_search(int arr[],int startInd,int endInd,int search){

    if(startInd>endInd) return false;

    else{
        int mid=random_ind(startInd,endInd);

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