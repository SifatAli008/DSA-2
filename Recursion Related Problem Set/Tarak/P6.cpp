// Calculate the nth term of a Fibonacci series.
// Created by Sifat Ali on 1/8/2024.
//
#include <iostream>
using namespace std;
int Fibonacci(int num){
    if (num == 0) {
        return 0;
    } else if(num==1){
        return 1;
    }
    else {
        int num1=Fibonacci(num-1);
        int num2=Fibonacci(num-2);
        return num1+num2 ;
    }
}

int main(){
   int n;

   cout<<"Enter a value : ";
   cin>>n;

   cout<<Fibonacci(n);
}