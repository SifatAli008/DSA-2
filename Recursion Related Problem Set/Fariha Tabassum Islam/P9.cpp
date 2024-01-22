//9. Write a recursive program to find the products of the elements of an array of size n.
// Created by Sifat Ali on 1/11/2024.
//

#include <iostream>
using namespace std;

int PrintArr(int n){
    if(n==1) return 1;
    return n*PrintArr(n-1);
}

int main(){
    int n;
    cin>>n;
    cout<<PrintArr(n);
}