#Quick_Sort

def Pertition(arr,start,end):
    pivot=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    i+=1
    arr[i],arr[end]=arr[end],arr[i]
    return i 

def Quick_Sort(arr,start,end):
    mid=(arr,start,end)
    Quick_Sort(arr,start,mid-1)
    Quick_Sort(arr,mid+1,end)


def main():
    n = int(input('Enter the size of arr: '))
    arr = []
    for i in range(n):
        value = int(input('Enter value: '))
        arr.append(value)
        
    Quick_Sort(arr, 0, len(arr) - 1)
    

main()