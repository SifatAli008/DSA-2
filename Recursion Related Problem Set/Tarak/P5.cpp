//5. Count the number of digits of a given number n.
// Created by Sifat Ali on 1/8/2024.
//
#include <iostream>
using namespace std;

int count(int num){
    if (num == 0) {
        return 1;
    } else {
        int rem = num % 10;
        num=num/10;
        return 1+count(num) ;
    }
}

int main(){
    int n;
    cout<<"Enter a value : ";
    cin>>n;

    cout<<"Total : "<<count(n)-1;
}