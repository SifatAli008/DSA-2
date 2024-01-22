// binary tree preorder,inorder,postorder
// Created by Sifat Ali on 1/9/2024.
//
#include <iostream>
using namespace std;

void preorder(int bin_tree[],int size,int myind){
     if(bin_tree[myind]==-1||myind>=size){
         return;
     }
     else{
         cout<<bin_tree[myind]<<" ";
         int left_chiled=2*myind;
         int right_chiled=2*myind+1;
         preorder(bin_tree,size,left_chiled);
         preorder(bin_tree,size,right_chiled);
       }
}
void Inorder(int bin_tree[],int size,int myind){
    if(bin_tree[myind]==-1||myind>=size){
        return;
    }
    else{
        int left_chiled=2*myind;
        int right_chiled=2*myind+1;
        Inorder(bin_tree,size,left_chiled);
        cout<<bin_tree[myind]<<" ";
        Inorder(bin_tree,size,right_chiled);
    }
}
void postorder(int bin_tree[],int size,int myind){
    if(bin_tree[myind]==-1||myind>=size){
        return;
    }
    else{
        int left_chiled=2*myind;
        int right_chiled=2*myind+1;
        postorder(bin_tree,size,left_chiled);
        postorder(bin_tree,size,right_chiled);
        cout<<bin_tree[myind]<<" ";
    }
}


int main(){
    int bin_tree[]={-1,100,300,50,120,200,30,-1,-1,20,80,150,-1,90};
    int n=sizeof(bin_tree)/sizeof(int);

    cout<<"In Order: ";
    Inorder(bin_tree,n,1);
    cout<<endl;

    cout<<"Pre Order: ";
    preorder(bin_tree,n,1);
    cout<<endl;

    cout<<"Post Order: ";
    postorder(bin_tree,n,1);
}