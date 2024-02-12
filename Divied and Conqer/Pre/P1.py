#print_odd

def odd_print(arr,start,end):
    if (start == end):
        if arr[start]%2 == 0:
            print (arr[start])
    
    else:
        mid=start+(end-start)//2
        odd_print(arr,start,mid)
        odd_print(arr,mid+1,end)

def main():
    arr = [0, 1, 2, 3, 4, 5]
    odd_print(arr, 0, len(arr) - 1)


main()