#Nth Fibo

def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1 
    return fibo(num - 1) + fibo(num - 2)

def main():
    n = 5
    print(fibo(n))
main()
