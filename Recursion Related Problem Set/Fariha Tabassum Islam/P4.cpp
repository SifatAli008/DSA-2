//Write a recursive program to check if a given string is a palindrome or not (not casesensitive, ignore whitespaces)
//Sample input--------Sample output
//Evil olive             True
//Too bad               False
// Created by Sifat Ali on 1/11/2024.
//
#include <iostream>
#include <cstring>
using namespace std;


bool Pali(char str[],int start,int end){
    while (start < end && str[start] == ' ') {
        start++;
    }
    while (start < end && str[end] == ' ') {
        end--;
    }

    if(start>=end) return true;
    else if(tolower(str[start])==tolower(str[end])){
        return Pali(str,start+1,end-1);
    }
    else return false;
}

int main(){
  char str[]={"Evil olive"};
    int n = strlen(str);
  bool result=Pali(str, 0,n-1);

  if(result)cout<<"true";
  else cout<<"false";
}