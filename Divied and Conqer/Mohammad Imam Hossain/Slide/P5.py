#Write a program that does the following
#(i) take N numbers as input and store them in an array A
#(ii) write a function findMaxMin that returns the maximum and minimum elements of an array using divide and conquer.
#(iii) use the function findMaxMin to print the maximum and minimum elements of the array A

def findMaxMin(arr, start, end):
    if start == end:
        return arr[start], arr[end]
    else:
        mid = (start + end) // 2
        left_min, left_max = findMaxMin(arr, start, mid)
        right_min, right_max = findMaxMin(arr, mid + 1, end)

        return min(left_min, right_min), max(left_max, right_max)

def main():
    n = int(input('Enter the size of arr: '))
    arr = []
    for i in range(n):
        value = int(input('Enter value: '))
        arr.append(value)
        
    min_val , max_val = findMaxMin(arr, 0, len(arr) - 1)
    print('Max:', max_val)
    print('Min:', min_val)


main()
