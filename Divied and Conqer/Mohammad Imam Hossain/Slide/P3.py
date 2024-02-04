#Write a function calc_sum using divide-and-conquer algorithm to calculate the sum of the even numbers of an array of n integers.

def even(num):
    return True if num % 2 == 0 else False

def even_sum(arr, start, end):
    if start == end:
        return arr[start] if even(arr[start]) else  0
    else:
        mid = (start + end) // 2
        return even_sum(arr, start, mid) + even_sum(arr, mid + 1, end)

def main():
    arr = [1, 2, 3, 4, 5]
    print(even_sum(arr, 0, len(arr)-1))

main() 