//Prints the numbers from 1 to n.
// Created by Sifat Ali on 1/8/2024.
//
#include <iostream>
using namespace std;

void PrintN(int n){
    if(n==0){
        return;
    } else{
        PrintN(n-1);
        cout<<n<<" ";
    }
}

int main(){
    int n;
    cout<<"Enter a value : ";
    cin>>n;

    PrintN(n);
}