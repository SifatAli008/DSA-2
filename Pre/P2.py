#calc_sum
def calc_sum(arr, start, end):
    
    mid = start + (end - start) // 2
    return arr[start]  if  start == end else calc_sum(arr, start, mid) + calc_sum(arr, mid + 1, end)
    

def main():
    arr = [0, 1, 2, 3, 4, 5]
    print(calc_sum(arr, 0, len(arr) - 1))

main()
