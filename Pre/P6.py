#Binary Search

def binary_Search(arr,start,end,value):
    if start<=end:
        mid = start + (end-start) //2
        if arr[mid] == value:
            return mid
        if arr[mid]>value:
            return binary_Search(arr,start,mid-1,value)
        else:
            return binary_Search(arr,mid+1,end,value)
    return -1

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    value = 10
    index = binary_Search(arr, 0, len(arr) - 1, value)
    if index != -1:
        print(f"Element {value} found at index {index}.")
    else:
        print(f"Element {value} not found in the array.")

main()