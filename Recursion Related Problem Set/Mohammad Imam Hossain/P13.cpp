#include <iostream>
using namespace std;

bool PalindromeHelper(string str, int start, int end) {
    if (start >= end) {
        return true;
    } else {
        if (str[start] == str[end]) {
            return PalindromeHelper(str, start + 1, end - 1);
        } else {
            return false;
        }
    }
}

bool Palindrome(int num) {
    string str = to_string(num);
    int length = str.length();
    return PalindromeHelper(str, 0, length - 1);
}

int main() {
    int num;
    cout << "Enter a value : ";
    cin >> num;

    bool result = Palindrome(num);
    if (result) {
        cout << "Palindrome";
    } else {
        cout << "Not Palindrome";
    }

    return 0;
}
