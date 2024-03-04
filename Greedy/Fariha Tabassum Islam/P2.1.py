def max_number_of_meetings(events, n, cleanup_time):
    count = 0
    current_end = events[0][0] + cleanup_time  # Initialize with the end time of the first event plus cleanup time
    
    for i in range(0, n):
        if events[i][0] >= current_end:
            count += 1
            current_end = events[i][0] + cleanup_time  # Adding cleanup time for the next event
        
    return count
    
    

def main():
    events = [('a', 2, 8), ('b', 3, 4), ('d', 8, 1), ('c', 7, 1)]
    cleanup_time = 1  # Assume 1 hour for cleanup and preparation
    events.sort(key=lambda x: x[2])  # Sort by end time
    max_meetings = max_number_of_meetings(events, len(events), cleanup_time)
    
    print("Chosen clubs:")
    for i in range(len(events)):
        if events[i][1] <= events[i][2]:  # Checking if there's enough time for the event
            print(events[i][0])
            max_meetings -= 1
            if max_meetings == 0:
                break

main()
