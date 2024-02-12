#X^Y

def pow(base, n):
    if base == 0:
        return 0
    if n == 0:
        return 1
    
    return pow(base, n//2) * pow(base, n//2) if n % 2 == 0 else base * pow(base, n//2) * pow(base, n//2)

def main():
    print(pow(5, 2))

main()
