#Find the number of zeroes

def NumberofZero(arr, size):
    if size == 0:
        return 0
    
    return 1 + NumberofZero(arr, size - 1) if arr[size] == 0 else  NumberofZero(arr, size - 1)

def main():
    arr = [1, 0, 0, 0, 0]
    print('Number of Zero :', NumberofZero(arr, len(arr) - 1))

main()
