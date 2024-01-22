//14. Write a recursive program to print the prime numbers of an array of n integers
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>

using namespace std;

bool isPrime(int n,int i){
    if (n == 1)
        return false;
    else {
        if (i == 1) return true;
        if (n % i == 0) return false;
        else return isPrime(n, i - 1);
    }
 }


int main(){
  int n;
 cin>>n;
 bool result=isPrime(n,n/2);
    if(result)cout<<n<<" is a prime number";
    else cout<<n<<" is not a prime number";
}