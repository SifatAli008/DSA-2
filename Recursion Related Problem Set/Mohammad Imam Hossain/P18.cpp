//coin change problem
//given a value N$,if we want to make change for N cents,and we have infinite supply of each of c ={C1=5,C2=10,C3=50,....,CN=1000}value coins , how many way can we make the change ?the odere of the coin does not matter
// Created by Sifat Ali on 1/10/2024.
//
#include <iostream>
using namespace std;

int coin_change(int coins[], int size, int amount) {
    if (amount == 0) {
        return 1;
    } else if (amount < 0 || (amount > 0 && size <= 0)) {
        return 0;
    } else {
        int way1 = coin_change(coins, size - 1, amount);
        int way2 = coin_change(coins, size, amount - coins[size - 1]);
        return way1 + way2;
    }
}

int main() {
    int coins[] = {5, 10, 50, 100, 500, 1000};
    int total_amount = 20;
    cout << coin_change(coins, sizeof(coins) / sizeof(coins[0]), total_amount) << endl;

    return 0;
}
