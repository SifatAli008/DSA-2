#Write a function print_odd using divide-and-conquer algorithm to print the odd numbers of an array of n integers.

def odd(num):
    return True if num % 2 != 0 else False

def print_odd(arr, start, end):
    if start == end:
        if odd(arr[start]):
            print(arr[start])
    else:
        mid = (start + end) // 2
        print_odd(arr, start, mid)
        print_odd(arr, mid + 1, end)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Odd numbers in the array:")
    print_odd(arr, 0, len(arr)-1)

main()