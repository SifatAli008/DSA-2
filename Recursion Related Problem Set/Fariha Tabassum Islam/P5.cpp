//Write a recursive program to print the even numbers in a given range.
//Sample input Sample output
//3 10             4 6 8 10
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;

void  even(int start,int end){
    if (start > end) {
        return;
    }
    if (start % 2 == 0) {
        cout << start << " ";
    }
    even(start + 1, end);
}

int main(){
    int i,n;
    cin>>i>>n;
    even(i,n);
 }
