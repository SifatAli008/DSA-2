//copy vector
// Created by Sifat Ali on 1/5/2024.
//
#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);

    for(auto element:v){
        cout<<element<<" ";
    }

    vector<int>v2(v);// v3 is a copy

    cout<<endl;
    for(auto element:v2){
        cout<<element<<" ";
    }

}