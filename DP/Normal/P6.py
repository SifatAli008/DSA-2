#Rod Cutting Problem

def rod_cut(arr, n):
    if n == 0:
        return 0
    
    max_val = float('-inf')
    for i in range(1, n+1):
        max_val = max(max_val, arr[i-1] + rod_cut(arr, n-i))
    
    return max_val

def main():
    arr = [1, 5, 6, 9, 11, 12, 14, 16]
    result = rod_cut(arr, len(arr))
    print("Maximum loot amount:", result)

main()
