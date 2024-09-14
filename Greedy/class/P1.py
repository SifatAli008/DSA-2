def large_sum(arr, n):
    largest_arr = []
    for i in arr:
        if len(largest_arr) < n:
            largest_arr.append(i)
        else:
            min_index = largest_arr.index(min(largest_arr))
            if i > largest_arr[min_index]:
                largest_arr[min_index] = i
    return sum(largest_arr)

def main():
    arr = [1, 4, 3, 9, 8, 6, 5, 7, 2]
    n = 3
    total_sum = large_sum(arr, n)
    print("Sum of the largest", n,":", total_sum)

main()
