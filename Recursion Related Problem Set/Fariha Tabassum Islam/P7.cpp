//Write a recursive program to print an array of size n in reverse order.
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;

void PrintArr(int n){
    if(n==0) return;
    cout<<n<<" ";
    PrintArr(n-1);

}

int main(){
    int n;
    cin>>n;
    PrintArr(n);
}