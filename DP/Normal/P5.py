#House Robbery Problem
# Given an array that determines the money stored in each,Find the maximume money can be robbed such that no two adjucent house are robbed


def house_loot(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    taken = house_loot(arr, n-2) + arr[n-1]
    not_taken =house_loot(arr, n-1)

    
    return max(taken,not_taken)

def main():
    arr = [2, 7, 3, 1, 4, 2, 1, 8]
    result = house_loot(arr, len(arr))
    print("Maximum loot amount:", result)

main()
