def combination_sum(arr, n, target):
    # Base cases
    if target == 0:
        return 1
    
    if target < 0:
        return 0
    
    ans = 0 
    
    if arr[n - 1] > target:
        return combination_sum(arr, n - 1, target)
    
    for i in range(n):
        ans += combination_sum(arr, n, target - arr[i])
    
    return ans

def main():
    arr = [1,5]  
    print(combination_sum(arr, len(arr), 11))

main()
