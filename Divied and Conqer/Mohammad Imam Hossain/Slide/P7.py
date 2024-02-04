#Write a function merge_sort that sorts an array of N numbers in descending order using merge sort. Write a main that takes N numbers as input from users into an array, sorts the array in descending order using the function merge_sort, and prints the sorted array.

def merge(arr,start,mid,end):
    left_arr_size = mid - start + 1
    right_arr_size = end - mid
    
    left_arr = [0] * left_arr_size
    right_arr = [0] * right_arr_size
    
    for i in range(left_arr_size):
        left_arr[i] = arr[start + i]

    for j in range(right_arr_size):
        right_arr[j] = arr[mid + 1 + j]

    left_ind = right_ind = 0
    k = start

    while left_ind < left_arr_size and right_ind < right_arr_size:
        if left_arr[left_ind] <= right_arr[right_ind]:
            arr[k] = left_arr[left_ind]
            left_ind += 1
        else:
            arr[k] = right_arr[right_ind]
            right_ind += 1
        k += 1

    while left_ind < left_arr_size:
        arr[k] = left_arr[left_ind]
        left_ind += 1
        k += 1

    while right_ind < right_arr_size:
        arr[k] = right_arr[right_ind]
        right_ind += 1
        k += 1

def merge_sort(arr,start,end):
    if start<=end:
        mid = (start+end)//2
        merge_sort(arr,start,mid-1)
        merge_sort(arr,mid+1,end)
        merge(arr,start,mid,end)

def main():
    n = int(input('Enter the size of arr: '))
    arr = []
    for i in range(n):
        value = int(input('Enter value: '))
        arr.append(value)
        
    merge_sort(arr, 0, len(arr) - 1)


main()