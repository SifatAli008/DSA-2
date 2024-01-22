//sum of left Leaves
// Created by Sifat Ali on 1/13/2024.
//
#include <iostream>

using namespace std;

int sum_left_leaves(int bin[] ,int size,int currNode){
    int leftchilde=2*currNode;
    int rightchilde=2*currNode+1;

    if((leftchilde>=size ||bin[leftchilde]==-1)&&
    (rightchilde>=size ||bin[rightchilde]==-1)){
     if(currNode%2==0){
         return  bin[currNode];
     }
      else{
         return 0;
      }
    }
   else{
      int total_sum=0;
       if(leftchilde<size && bin[leftchilde]!=-1){
           total_sum+=  sum_left_leaves(bin,size,leftchilde);
       }
       if(rightchilde<size && bin[rightchilde]!=-1){
           total_sum+= sum_left_leaves(bin,size,rightchilde);
        }
        return total_sum;
   }
}

int main(){
  int bin[]={-1,10,5,18,3,7,12,20,-1,-1,6,-1,-1,15,19,21};
  int n= size(bin);

  cout<<sum_left_leaves(bin,n,1);
}