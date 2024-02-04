#Write a function calc_sum using divide-and-conquer algorithm to calculate the sum of an array of n
#integers.

def calc_sum(arr,start,end):
    if start==end:
        return arr[start]

    mid=(start+end)//2
    return  calc_sum(arr,start,mid)+calc_sum(arr,mid+1,end)

def main():
    arr = [1, 2, 3, 4]
    print(calc_sum(arr,0,len(arr)-1))

main()