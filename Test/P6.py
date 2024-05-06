def combination_sum(arr, target):
    memo = {}

    def helper(target):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target in memo:
            return memo[target]
        
        count = 0
        for num in arr:
            count += helper(target - num)
        
        memo[target] = count
        return count
    
    return helper(target)

def main():
    arr = [1, 2, 3, 5]
    target = 11
    print("Number of combinations:", combination_sum(arr, target))

main()
