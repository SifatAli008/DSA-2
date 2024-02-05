#Check for Majority Element in a sorted array

def count_majority(arr, start, end, target):
    if start > end:
        return 0
    elif start == end:
        return 1 if arr[start] == target else 0
    else:
        mid = (start + end) // 2
        left_count = count_majority(arr, start, mid, target)
        right_count = count_majority(arr, mid + 1, end, target)
        return left_count + right_count

def is_majority(arr, n, target):
    count = count_majority(arr, 0, n, target)
    return count > (n + 1) // 2

def main():
    arr = [1, 1, 1, 2, 2]
    x = int(input('Enter value: '))
    if is_majority(arr, len(arr) - 1, x):
        print('True')
    else:
        print('False')

main()


