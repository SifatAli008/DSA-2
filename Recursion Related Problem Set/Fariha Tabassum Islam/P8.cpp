//8. Write a recursive program to find the sum of the elements of an array of size n.
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;

int PrintArr(int n){
    if(n==0) return 0;
    return n+PrintArr(n-1);
}

int main(){
    int n;
    cin>>n;
    cout<<PrintArr(n);
}