#PROBLEM 10. Maximum-sum subarray

def max_crossing_sub_arr(arr, low, mid, high):
    left_sum = right_sum = float('-inf')
    left_index = right_index = 0

    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i

    sum = 0
    for j in range(mid + 1, high+1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
            right_index = j

    return (left_index, right_index, left_sum + right_sum)


def max_of_sub_array(arr, start, end):
    if start == end:
        return (arr[start], start, end)  
    else:
        mid = (start + end) // 2

        left_max = max_of_sub_array(arr, start, mid)
        right_max = max_of_sub_array(arr, mid + 1, end)
        crossing_max = max_crossing_sub_arr(arr, start, mid, end)

        max_sum, left_index, right_index = left_max
        if right_max[0] > max_sum:
            max_sum, left_index, right_index = right_max
        if crossing_max[0] > max_sum:
            max_sum, left_index, right_index = crossing_max
        
        return (max_sum, left_index, right_index)



def main():
    arr = [2, 3, 4, 5, 7]
    start = 0
    end = len(arr) - 1
    max_sum, left_index, right_index = max_of_sub_array(arr, start, end)
    print("Maximum sum value:", max_sum)
    print("Index range:", (left_index, right_index))

main()
