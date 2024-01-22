// print
// Created by Sifat Ali on 1/7/2024.
//
#include <iostream>
using namespace std;

void print(int size){
    int i=0;
    if(i==size){
        cout<<size;
    }else{
        print(i++);
        cout<<i;
    }
}


int main(){
    int n;
    cin>>n;
    print(n);
}