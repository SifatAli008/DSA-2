//Print
// Created by Sifat Ali on 1/7/2024.
//
#include <iostream>
using namespace std;

void Print(int i){
   if(i==0){
       cout<<0<<" ";
   }
   else{
       Print(i-1);
     cout<<i<<" ";
   }
};


int main(){
    int n;
    cin>>n;
    Print(n);
}
