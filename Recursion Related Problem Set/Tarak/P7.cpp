//7. Calculate a to the power b
// Created by Sifat Ali on 1/8/2024.
//

#include <iostream>
using namespace std;


int calculate(int base,int pow ){
    if(pow==0){
        return 1;
    }
    else{
        int result = calculate(base,pow-1);
        return base*result;
    }
}

int main(){
    int base,power;

    cout<<"Enter base value: ";
    cin>>base;
    cout<<endl;

    cout<<"Enter power value: ";
    cin>>power;

    cout<<calculate(base,power);
}