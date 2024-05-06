#Painting the Fance not be adjencency list

def Painting_the_Fence(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return k
    same = Painting_the_Fence(n-1, k) 
    different = Painting_the_Fence(n-2, k)

    return (same + different ) * (k - 1)

def main():
    n = 6
    k = 7
    print(Painting_the_Fence(n, k))

main()
