#The quick sort uses divide and conquer just like merge sort but without using additional storage. The steps are following:
#1. Select an element q, called a pivot, from the array. In this algorithm we have chosen the last index as the pivot.
#2. The PARTITION function finds the location of the pivot in such a way that all the elements smaller than the pivot are on the left side and all the elements on the right-hand side of the pivot are greater in value. (Items with equal values can go either way).
#3. Recursively call the QUICKSORT function which performs quicksort on the array on the left side of the pivot and then on the array on the right side, thus dividing the task into sub tasks. This is carried out until the arrays can no longer be split.


def pertition(arr,start,end):
    pivot=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    i+=1
    arr[i],arr[end]=arr[end],arr[i]
    return i     

def quick_sort(arr,start,end): 
    if start<=end:
        mid=pertition(arr,start,end)
        quick_sort(arr,start,mid-1)
        quick_sort(arr,mid+1,end)
        
def main():
    n = int(input('Enter the size of arr: '))
    arr = []
    for i in range(n):
        value = int(input('Enter value: '))
        arr.append(value)
        
    quick_sort(arr, 0, len(arr) - 1)

    
main()    