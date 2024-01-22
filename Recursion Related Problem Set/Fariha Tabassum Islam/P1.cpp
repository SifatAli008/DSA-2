//Write a recursive implementation of the factorial function. Recall that n! =
//1 × 2 × ... × n, with the special case that 0! = 1.
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>

using namespace std;

int fact(int n){
    if(n==0)return 1;
    else return n*fact(n-1);
}
int main(){
   int n;
   cout<<"Enter a value : ";
   cin>>n;
   cout<<"factorial : "<<fact(n);
}