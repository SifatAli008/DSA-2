def max_number_of_meeting(pairs, n):
    if n == 0:
        return 0, []  # Return 0 meetings if there are no meetings

    count = 1
    scheduled_meetings = [pairs[0][0]]  # Add the first meeting to scheduled meetings
    current_end = pairs[0][2]

    for i in range(1, n):
        if pairs[i][1] >= current_end:  # If the meeting's start time is after or equal to current end time
            count += 1
            current_end = pairs[i][2]
            scheduled_meetings.append(pairs[i][0])

    return count, scheduled_meetings

def main():
    meeting = ["meeting1", "meeting2", "meeting3", "meeting4", "meeting5"]
    start = [1, 3, 0, 5, 8]
    end = [2, 4, 6, 7, 9]
    pairs = list(zip(meeting, start, end))
    pairs.sort(key=lambda x: x[2])  # Sort by end time
    
    num_meetings, scheduled_meetings = max_number_of_meeting(pairs, len(meeting))
    
    print("Maximum number of meetings:", num_meetings)
    print("Scheduled meetings:", scheduled_meetings)
    
main()
