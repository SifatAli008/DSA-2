#Binary Search
#Write a function binary_search that finds the index of an element X in a sorted (ascending) array A of N integers using divide and conquer. If the element X is not present in the array, return -1.
#Write a main that takes the array A and an integer X as input from the user. After that, sort the array A using the quicksort algorithm and find the index of X in A using the function binary_search and print it.

def Binary_Search(arr, start, end, value):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            return Binary_Search(arr, mid + 1, end, value)  # Search in the right half
        else:
            return Binary_Search(arr, start, mid - 1, value)  # Search in the left half
    else:
        return -1  # Element not found

def main():
    n = int(input('Enter the size of arr: '))
    arr = []
    for i in range(n):
        value = int(input('Enter value: '))
        arr.append(value)
        
    x = int(input('Enter the value to search for: '))
    
    arr.sort()
    
    index = Binary_Search(arr, 0, len(arr) - 1, x)
    if index != -1:
        print(f"The index of {x} in the array is: {index}")
    else:
        print(f"{x} is not present in the array.")

main()
