//SWAP two vector
// Created by Sifat Ali on 1/5/2024.
//
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int>v;
    v.push_back(1);
    v.push_back(3);
    v.push_back(2);
    v.push_back(7);
    v.push_back(5);
    v.push_back(6);

    for(auto element:v){
        cout<<element<<" ";
    }
    vector<int>v2(3,50);
    swap(v,v2);
    for(auto element:v){
        cout<<element<<" ";
    }
    cout<<endl;
    for(auto element:v2){
        cout<<element<<" ";
    }

    sort(v.begin(),v.end());

    return 0;
}