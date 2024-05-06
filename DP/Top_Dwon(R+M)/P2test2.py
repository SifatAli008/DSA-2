#Climbing Stairs

def Climbing_way(nStairs, Ways):
    # Base cases
    if nStairs == 0:
        return 1
    if nStairs == 1:
        return 1

    if Ways[nStairs] != 0:
        return Ways[nStairs]

    Ways[nStairs] = Climbing_way(nStairs - 1, Ways) + Climbing_way(nStairs - 2, Ways)
    return Ways[nStairs]

def main():
    nStairs = 5
    Ways = [0] * (nStairs + 1)  
    print("Number of ways to climb the stairs:", Climbing_way(nStairs, Ways))

main()
