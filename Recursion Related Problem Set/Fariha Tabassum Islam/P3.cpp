//Write a recursive program to print the nth Fibonacci number.
// Created by Sifat Ali on 1/11/2024.
//

#include <iostream>
using namespace std;

int fibo(int n){
 if(n==0) return 0;
 if(n==1) return 1;
 else{
   return fibo(n-1)+ fibo(n-2);
 }
}
int main(){
    int n;
    cout<<"Enter a value : ";
    cin>>n;

    cout<<fibo(n);
}