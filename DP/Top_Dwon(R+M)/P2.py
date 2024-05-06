#Minimum Cost Climbing Stairs 
#0 STAIRS - 0

def Climbing_way(nStairs, Ways, cost):
    # Base case
    if nStairs == 0:
        return 0
    if nStairs == 1:
        return cost[1]

    # If already computed, return the stored value
    if Ways[nStairs] != -1:
        return Ways[nStairs]

    # Compute and store the minimum cost
    Ways[nStairs] = min(Climbing_way(nStairs - 1, Ways, cost) + cost[nStairs], #n-1
                        Climbing_way(nStairs - 2, Ways, cost) + cost[nStairs]) #n-2

    return Ways[nStairs]

def main():
    nStairs = 5
    cost = [0, 3, 2, 4, 6, 1]  # Cost associated with each step
    Ways = [-1] * (nStairs + 1)  # Initialize Ways list with -1
    print("Minimum cost to climb the stairs:", Climbing_way(nStairs, Ways, cost))

main()
