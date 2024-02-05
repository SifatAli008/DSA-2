#Find a peak element which is not smaller than its neighbours

def find_peak(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2

    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == end or arr[mid + 1] <= arr[mid]):
        return arr[mid]

    if mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak(arr, start, mid - 1)
    else:
        return find_peak(arr, mid + 1, end)

def peak(arr, size):
    return find_peak(arr, 0, size)

def main():
    arr = [10, 20, 15, 2, 23, 90, 67]
    print("Peak element:", peak(arr, len(arr) - 1))

main()
