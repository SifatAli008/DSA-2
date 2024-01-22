//Remove white spaces from a string & convert upper cases to lower.
// Created by Sifat Ali on 1/8/2024.
//

#include <iostream>
#include <cctype>
using namespace std;


void RemoveSpaceAndLowerCase(char str[], int n) {
    if (n < 0) {
        cout << "Processed String: " << str << endl;
        return;
    }
    
    if (str[n] == ' ') {
        int i = n;
        while (str[i] != '\0') {
            str[i] = str[i + 1];
            i++;
        }
        RemoveSpaceAndLowerCase(str, n-1);
    }
    else {
        str[n] = tolower(str[n]);
        RemoveSpaceAndLowerCase(str, n - 1);
    }
}


int main(){
    char str[]="ma DAM";
    int n=size(str);

    RemoveSpaceAndLowerCase(str,n-1);

}