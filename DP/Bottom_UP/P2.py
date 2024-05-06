#Minimum Cost Climbing Stairs


def main():
    nStairs = 5
    cost = [0, 3, 2, 4, 6, 1]  # Cost associated with each step
    Ways = [-1] * (nStairs + 1)  # Initialize Ways list with -1
    if nStairs == 0:
        print(cost[0])
        return
    
    if nStairs == 1:
        print(cost[1])
        return
    
    for i in range(2, nStairs + 1):  # Fix the range to include nStairs
        Ways[i] = cost[i] + min(Ways[i - 1], Ways[i - 2])
        
    print("Minimum cost to climb the stairs:", min(Ways[nStairs - 1], Ways[nStairs - 2]))

main()
