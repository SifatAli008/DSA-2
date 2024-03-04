#shop in candy store (In a candy store, there are N different types of candies available and the prices of all the N different types of candies are provided to you.)
def buy_candies(candies, k, n):
    min_cost = 0
    max_cost = 0
    
    buy = 0
    free = n - 1
    

    while buy <= free:
        min_cost += candies[buy]
        buy += 1
        free -= k  

    buy = n - 1
    free = 0
    

    while free <= buy:
        max_cost += candies[buy]
        buy -= 1
        free += k 

    return min_cost, max_cost

def main():
    candies = [3, 4, 2, 1]
    candies.sort()
    min_cost, max_cost = buy_candies(candies, 2, len(candies))
    print(min_cost, max_cost)

main()
