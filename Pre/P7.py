#Merge sort


def Merge(arr,start,mid,end):
    left_arr = arr[start:mid + 1]
    right_arr = arr[mid + 1:end + 1]
    
    i = j = 0
    
    for k in range(start, end + 1):
        if i < len(left_arr) and (j >= len(right_arr) or left_arr[i] <= right_arr[j]):
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
    

def Merge_Sort(arr,start,end):
    if start<=end:
        mid = start + (end - start) // 2
        Merge_Sort(arr,start,mid-1)
        Merge_Sort(arr,mid+1,end)
        Merge(arr,start,mid,end)

def main():
    arr = [12, 11, 13, 5, 6, 7,11,5]
    print("Given array is", arr)
    Merge_Sort(arr, 0, len(arr) - 1)
    print("Sorted array is", arr)
    
main()