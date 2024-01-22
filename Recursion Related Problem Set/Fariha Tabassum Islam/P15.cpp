//Write a recursive program to count the odd/even numbers of an array of n integers
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;

int PrintEvenOdd(int arr[],int n ){
    if(n<0){
        return 0;
    }
    else{
        if(arr[n]%2==0){
            return 1 + PrintEvenOdd(arr, n - 1);
        } else{
            return PrintEvenOdd(arr,n-1);
        }
    }
}

int main(){
    int arr[] = {1, 0, 2, 4, 5, 6, -1, 8 };
    int n = sizeof(arr) / sizeof(arr[0]);


  int result=  PrintEvenOdd(arr, n - 1);
    cout << "Even numbers: "<<result;
    cout << endl;
    cout << "Odd numbers: "<<n-result;


}