#Median of two sorted arrays of same size
def merge(arr1, arr2):
    merged = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged

def median_value(arr1, arr2):
    merged = merge(arr1, arr2)
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2] + merged[(n // 2) - 1]) / 2.0
    else:
        return merged[n // 2]

def main():
    arr1 = [2, 3, 6, 7, 9]
    arr2 = [1, 4, 8, 10]
    result = median_value(arr1, arr2)
    print("The median is:", result)

main()
