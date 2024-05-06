#Minimum Cost Climbing Stairs//space


def main():
    nStairs = 5
    cost = [0, 3, 2, 4, 6, 1]  # Cost associated with each step
    prev1=cost[0]
    prev2=cost[1] # Initialize Ways list with -1
    
    for i in range(2, nStairs + 1):  # Fix the range to include nStairs
        current = cost[i] + min(prev1,prev2)
        prev1, prev2 = prev2, current
        
    print("Minimum cost to climb the stairs:", min(prev1, prev2))

main()
