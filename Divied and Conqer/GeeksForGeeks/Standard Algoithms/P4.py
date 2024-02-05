#Write program to calculate pow(x, n)

def Pow(base,num):
    if base==0:
        return 0
    if num==0:
        return 1
    return base*Pow(base,num-1)

def main():
    base = float(input("Enter the base value: "))
    num = int(input("Enter the exponent value: "))
    print(f"{base} raised to the power of {num} is ",Pow(base, num))

main()
