//Calculate the sum of digits of a given number n.
// Created by Sifat Ali on 1/8/2024.
//

#include <iostream>
using namespace std;

int SumOfDigit(int num){
    if (num == 0) {
        return 0;
    } else {
        int rem = num % 10;
        num=num/10;
        return  rem+= SumOfDigit(num);
    }
}

int main(){
    int n;
    cout<<"Enter a value : ";
    cin>>n;

    cout<<"Total : "<<SumOfDigit(n);
}