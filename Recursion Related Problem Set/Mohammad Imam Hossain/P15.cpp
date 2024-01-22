#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool bin_search(vector<int>& v, int s, int start, int end) {
    if (start >= end) {
        return false;
    } else {
        int midindex = (start + end) / 2;
        int midvalue = v[midindex];
        if (midvalue == s) {
            return true;
        } else if (s < midvalue) {
            return bin_search(v, s, start, midindex - 1);
        } else {
            return bin_search(v, s, midindex + 1, end);
        }
    }
}

int main() {
    int arr[] = {10, 5, -20, 100, 1000, -500};
    vector<int> v(arr, arr + 6);

    sort(v.begin(), v.end());

    int search =-20;

    cout << bin_search(v, search, 0, v.size() - 1);

    return 0;
}
