#Combination_Sum IV
#[1,2,3,5]=11


#1-6,2-3=11
#2-5,1-1=11
#2-3,1-5=11
#3-2,1-5=11
#1-1,2-5=11
#5-
#3-3,1-2=11
#4-2,3-1=11
#5-2,1-1=11
#6-1,1-5=11
#7-1,2-2=11
#8-1,1-3=11 
#1-2,3-3=11   
#9-1,1-2=11
#11-1=11

def combination_sum(arr, n, target,ways):
    
    if target == 0:
        return 1
    
    if n == 0 :
        return 0
    
    if ways[n - 1] != -1:  
        return ways[n - 1]
    
    if arr[n - 1] > target:
        return combination_sum(arr, n - 1, target,ways)
    
    taken = combination_sum(arr, n, target - arr[n - 1],ways)
    not_taken = combination_sum(arr, n - 1, target,ways)
    
    ways[n-1]= taken + not_taken
    
    return ways[n-1]

def main():
    arr = [1, 2, 5]  
    ways = [-1] * (len(arr) + 1)
    print(combination_sum(arr, len(arr), 5,ways))

main()
