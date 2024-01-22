//value insertion in middle;
// Created by Sifat Ali on 1/5/2024.
//
#include <iostream>
#include <vector>
using namespace std;
int main(){
   vector<int>v1;
  v1.push_back(3);

    vector<int>v;

    v.push_back(1);
    v.push_back(2);
    //add new line 3
    v.push_back(4);

    vector<int>::iterator it=v.begin()+2;
    v.insert(it,v1.begin(),v1.end());

    for(auto element:v){
        cout<<element<<" ";
    }
}