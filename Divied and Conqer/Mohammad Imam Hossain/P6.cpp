//Karatsuba Algorithm fast multiplication
// Created by Sifat Ali on 1/12/2024.
//

#include <iostream>
#include <cmath>
using namespace std;

int num_digit(int num){
    return floor(log10(num)+1);
}

long Fast_multiply(int num1,int num2){
    if(num1<10 && num2<10) return num1*num2;

    else{
        int digit=max(num_digit(num1),num_digit(num2));

        int m=ceil(digit/2.0);
        int power=pow(10,m);

        int a=num1/power;
        int b=num1%power;

        int c=num2/power;
        int d=num2%power;

        long ac= Fast_multiply(a,c);
        long bd= Fast_multiply(b,d);
        long a_b_c_d = Fast_multiply(a + b, c + d);

        return  pow(10,2*m)*ac+pow(10,m)*(a_b_c_d-ac-bd)+bd;
    }
}

int main(){
    cout<<Fast_multiply(1234 ,5678); //output: 7006652
}
