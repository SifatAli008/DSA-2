#- Min Cost of Ropes
import heapq

def min_cost_of_ropes(arr):
    if not arr:
        return 0
    
    heapq.heapify(arr)  # Convert the array into a min-heap
    min_cost = 0

    while len(arr) > 1:
        rope1 = heapq.heappop(arr)
        rope2 = heapq.heappop(arr)
        
        # Merge the two ropes and calculate cost
        merged_rope = rope1 + rope2
        min_cost += merged_rope
        
        # Add the merged rope back to the heap
        heapq.heappush(arr, merged_rope)

    return min_cost

def main():
    arr = [4, 3, 2, 6]
    print(min_cost_of_ropes(arr))  # Output: 29

main()