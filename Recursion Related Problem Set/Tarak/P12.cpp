//12. Check whether a given string is palindrome or not.
// Created by Sifat Ali on 1/8/2024.
//
#include<iostream>
#include <cctype>
using namespace std;


bool Palindrom(char str[],int s,int n) {
    if (s >= n) {
        return true;
    } else {
        if (str[s] == str[n]) {
            return  Palindrom(str, s + 1, n - 1);
        } else {
            return false;
        }
    }

}

int main(){
    char str[]="MADam";
    int n=size(str);

    for (int i = 0; i < n; ++i) {
        str[i] = toupper(str[i]);
    }

    bool ch = Palindrom(str,0,n-2);
    if(ch== true){
        cout<<"Palindrom";
    }else{
        cout<<"Not Palindrom";
    }
}