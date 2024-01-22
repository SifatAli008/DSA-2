//Coin change
// Created by Sifat Ali on 1/10/2024.
//
#include <iostream>
using namespace std;

int coin_change(int coins[],int size,int amount){
  if(amount==0){
      return 1;
  }
  else if(amount<0){//negative amount
      return 0;
  }
  else if(amount>0 && size==0){ //no_coin available
      return 0;
  }
  else{
      int way1= coin_change(coins,size,amount-coins[size-1]);
      int way2= coin_change(coins,size-1,amount);
      return way1+way2;
  }
}


int main(){
    int coins[]={2,3,5};
    int amount;
    cout<<"Enter a Amount : "<<" ";
    cin>>amount;
    cout<<"Ways : "<<coin_change(coins, size(coins),amount);
}