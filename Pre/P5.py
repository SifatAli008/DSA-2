#min_max
def min_max(arr, start, end):
    if start == end:
        return arr[start], arr[start]
    
    mid = start + (end - start) // 2
    left_min, left_max = min_max(arr, start, mid)
    right_min, right_max = min_max(arr, mid + 1, end)
    
    return min(left_min, right_min), max(left_max, right_max)
    

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(min_max(arr, 0, len(arr) - 1))
    

main()
