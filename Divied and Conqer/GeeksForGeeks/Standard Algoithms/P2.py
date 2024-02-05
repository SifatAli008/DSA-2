#Merge
def merge(arr, start, mid, end):
    leftarr_size = mid - start + 1
    rightarr_size = end - mid

    leftarr = arr[start:mid + 1]
    rightarr = arr[mid + 1:end + 1]

    leftind = 0
    rightind = 0
    current = start

    while leftind < leftarr_size and rightind < rightarr_size:
        if leftarr[leftind] <= rightarr[rightind]:
            arr[current] = leftarr[leftind]
            leftind += 1
        else:
            arr[current] = rightarr[rightind]
            rightind += 1
        current += 1

    while leftind < leftarr_size:
        arr[current] = leftarr[leftind]
        leftind += 1
        current += 1

    while rightind < rightarr_size:
        arr[current] = rightarr[rightind]
        rightind += 1
        current += 1

def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def main():
    arr = [14, 7, 3, 12, 9, 11, 6, 2]
    mergeSort(arr, 0, len(arr) - 1)

    for num in arr:
        print(num, end=" ")

main()