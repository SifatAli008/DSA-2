#Write a function count_inversion that counts the inversions in an array of N numbers using divide and conquer. Write a main function that takes N numbers from users and uses the function count_inversion to count the number of inversions and print it

def merge(left, right):
    merged = []
    inversions = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions

def count_inversion(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = count_inversion(arr[:mid])
    right, inv_right = count_inversion(arr[mid:])
    merged, inv_merge = merge(left, right)
    return merged, inv_left + inv_right + inv_merge

def main():
    N = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the array elements: ").split()))
    _, inversions = count_inversion(arr)
    print("#inversions:", inversions)

main()
