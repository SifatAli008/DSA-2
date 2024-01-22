//GDC & LCM
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
using namespace std;

int GCD(int m,int n){
    if(n==0)return m;
    else {
        int reminder =m%n;
        return GCD(n,reminder);
    }
}
int LCM(int m,int n,int GCD){
    return (m*n)/GCD;
}
int main(){
    int m,n;
    cin>>m>>n;
    int gcd=GCD(m,n);
    cout<<"LCM : "<<LCM(m,n,gcd)<<endl;
    cout<<"GCD : "<<gcd;
}