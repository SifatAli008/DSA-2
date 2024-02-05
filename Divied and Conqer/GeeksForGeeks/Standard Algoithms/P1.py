#Binary Search

def Binary_search(arr, start, end, value):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid  
        elif arr[mid] < value:
            return Binary_search(arr, mid + 1, end, value) 
        else:
            return Binary_search(arr, start, mid - 1, value)  
    else:
        return -1  # Return -1 if the value is not found

def main():
    arr = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23]
    value = 13
    index = Binary_search(arr, 0, len(arr) - 1, value)
    if index != -1:
        print(f"Value {value} found at index {index}.")
    else:
        print(f"Value {value} not found in the array.")

main()
