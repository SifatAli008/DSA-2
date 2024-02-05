#K-th Element of Two Sorted Arrays

def merge(arr1, arr2,size1,size2):
    merged = []
    if size1==0 :
        return   merged = arr2
    if size2==0 :
        return merged = arr1
    
    return merged

def find_k_element(arr1, arr2, k):
    merged = merge(arr1, arr2,len(arr1),)
    sorted_merged = sorted(merged, reverse=True)
    return sorted_merged[k - 1]

def main():
    arr1 = [2, 3, 6, 7, 9]
    arr2 = [1, 4, 8, 10]
    k = 5 
    result = find_k_element(arr1, arr2, k)
    print("The k-th element is:", result)

main()


