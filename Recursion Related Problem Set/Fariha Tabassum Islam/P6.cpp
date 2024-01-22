//Write a recursive program to print an array of size n in given order.
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;

void PrintArr(int n){
  if(n==0) return;
      PrintArr(n-1);
      cout<<n<<" ";
}

int main(){
 int n;
 cin>>n;
    PrintArr(n);
}