#max_number_of_meeting GG
def max_number_of_meeting(pairs, n):
    count = 0
    current_end = pairs[0][0]
    

    for i in range(0, n):  # Use range(n) instead of range(1, n)
        if pairs[i][0] >= current_end:
            count += 1
            current_end = pairs[i][1]
            print(pairs[i])  
    
    return count

def main():
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    pairs = list(zip(start, end))
    pairs.sort(key=lambda x: x[1])
    print(max_number_of_meeting(pairs, len(start)))  # Use len(start)
    
main()
