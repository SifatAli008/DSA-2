#House Robbery Problem
# Given an array that determines the money stored in each,Find the maximume money can be robbed such that no two adjucent house are robbed

def house_loot(arr, n, ways):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    if ways[n] != -1:
        return ways[n]
    
    taken = house_loot(arr, n-2, ways) + arr[n-1]
    not_taken =house_loot(arr, n-1, ways)
    
    ways[n] = max(not_taken,taken)
    
    return ways[n]

def main():
    arr = [2, 7, 3, 1, 4, 2, 1, 8]
    ways = [-1] * (len(arr) + 1)
    result = house_loot(arr, len(arr), ways)
    print("Maximum loot amount:", result)

main()
