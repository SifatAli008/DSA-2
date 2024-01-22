//Print Leaves
// Created by Sifat Ali on 1/13/2024.
//
#include <iostream>

using namespace std;

void print_leaves(int bin[] ,int size,int currNode){
    int leftchilde=2*currNode;
    int rightchilde=2*currNode+1;

    if((leftchilde>=size ||bin[leftchilde]==-1)&&
       (rightchilde>=size ||bin[rightchilde]==-1)){
        cout<< bin[currNode]<<" ";
    }
    else{
        if(leftchilde<size && bin[leftchilde]!=-1){
            print_leaves(bin,size,leftchilde);
        }
        if(rightchilde<size && bin[rightchilde]!=-1){
            print_leaves(bin,size,rightchilde);
        }
    }
}

int main(){
    int bin[]={-1,10,5,18,3,7,12,20,-1,-1,6,-1,-1,15,19,21};
    int n= size(bin);

    print_leaves(bin,n,1);
}