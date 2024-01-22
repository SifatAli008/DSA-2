//earase
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
    v.push_back(4);
    v.push_back(5);
    v.push_back(6);

    for(int i=0;i<v.size();i++){
        cout<<v[i]<<" ";
    }
    v.erase(v.begin()+1,v.begin()+3);
    cout<<endl;

    for(int i=0;i<v.size();i++){
        cout<<v[i]<<" ";
    }
}