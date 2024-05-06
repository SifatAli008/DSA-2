# Painting Fence

def Painting_the_Fence(n, k, ways):
    if n == 0:
        return 0
    elif n == 1:
        return k
    if ways[n] != -1:
        return ways[n]
    
    same = Painting_the_Fence(n-1, k, ways)
    different = Painting_the_Fence(n-2, k, ways)
    
    ways[n] = (same + different) * (k - 1)
    
    return ways[n]


def main():
    n = 15
    k = 5
    
    ways = [-1] * (n + 1)
    print(Painting_the_Fence(n, k,ways))

main()
