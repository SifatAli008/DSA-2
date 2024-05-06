#Climbing Stairs

def Climbing_way(nStairs, i, Ways):
    # Base cases
    if i > nStairs:
        return 0
    if i == nStairs:
        return 1

    Ways[i] = Climbing_way(nStairs, i + 1, Ways) + Climbing_way(nStairs, i + 2, Ways)
    return Ways[i]

def main():
    nStairs = 5
    Ways = [0] * (nStairs + 1)  # Initialize Ways list with zeros
    print("Ways:", Climbing_way(nStairs, 0, Ways))

main()
