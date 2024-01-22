//coin change with use coins
// Created by Sifat Ali on 1/10/2024.
//
#include <iostream>
#include <vector>
using namespace std;

int coin_change(int coins[], int size, int amount, vector<int>& selectedCoins) {
    if (amount == 0) {
        for (int coin : selectedCoins) {
            cout << coin << " ";
        }
        cout << endl;
        return 1;
    } else if (amount < 0) { // negative amount
        return 0;
    } else if (amount > 0 && size == 0) { // no coin available
        return 0;
    } else {
        // Include the last coin
        selectedCoins.push_back(coins[size - 1]);
        int way1 = coin_change(coins, size, amount - coins[size - 1], selectedCoins);
        selectedCoins.pop_back(); // Backtrack

        // Exclude the last coin
        int way2 = coin_change(coins, size - 1, amount, selectedCoins);

        return way1 + way2;
    }
}

int main() {
    int coins[] = {2, 3, 5};
    int amount;
    cout << "Enter an Amount: ";
    cin >> amount;

    vector<int> selectedCoins;
    cout << "Ways: "<<endl << coin_change(coins, sizeof(coins) / sizeof(coins[0]), amount, selectedCoins);
    return 0;
}
