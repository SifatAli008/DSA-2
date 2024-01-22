//Write a recursive program to calculate the power of x (x^y), where y is a non-negativeinteger.
// Created by Sifat Ali on 1/11/2024.
//

#include <iostream>
using namespace std;

int power(int b,int p) {
    if (p == 0)return 1;
    else return b*power(b, p - 1);

}
int main(){
  int b,p;
  cin>>b>>p;
  cout<<"Power : "<<power(b,p);
}