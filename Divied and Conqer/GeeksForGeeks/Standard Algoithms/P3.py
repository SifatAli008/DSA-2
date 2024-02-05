#Quick_sort
def Partition(arr, start, end):
    Pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= Pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i

def Quick_sort(arr, start, end):
    if start < end :
        mid = Partition(arr, start, end)
        Quick_sort(arr, start, mid - 1)
        Quick_sort(arr, mid + 1, end)

def main():
    arr = [2, 8, 4, 54, -1, 23]
    Quick_sort(arr, 0, len(arr) - 1)
    print(arr)

main()
