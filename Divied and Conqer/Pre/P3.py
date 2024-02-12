#even sum

def calc_sum(arr, start, end):
    if (start == end):
        if arr[start]%2 == 0:
            return arr[start]
        else:
            return 0   
    
    mid = start + (end - start) // 2
    return  calc_sum(arr, start, mid) + calc_sum(arr, mid + 1, end)


def main():
    arr = [0, 1, 2, 3, 4, 5]
    print(calc_sum(arr, 0, len(arr) - 1))

main()
