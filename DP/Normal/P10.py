#Combination_Sum IV

def combination_sum(arr, n, target):
    
    if target == 0:
        return 1
    
    if n == 0 :
        return 0
    
    if arr[n - 1] > target:
        return combination_sum(arr, n - 1, target)
    
    taken = combination_sum(arr, n, target - arr[n - 1])
    not_taken = combination_sum(arr, n - 1, target)
    
    
    return taken + not_taken

def main():
    arr = [1, 2, 5]  
    print(combination_sum(arr, len(arr), 5))

main()
