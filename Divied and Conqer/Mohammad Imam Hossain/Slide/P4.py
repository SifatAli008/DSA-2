#Write a program that takes X and Y as input and calculates the value of X^Y using divide and conquer and prints it.

def pow (base,num):
    if base==0:
        return 0
    if num==0:
        return 1
    
    return base*pow(base,num-1)

def main():
    print(pow(5,2))

main()    