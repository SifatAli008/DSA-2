#PROBLEM 05. Determine the smallest set of unit-length closed intervals
def smallest_closed_intervals_greedy(points):
    points.sort()

    intervals = []

    last_interval_end = float('-inf')

    for point in points:
        if point > last_interval_end:
            interval_start = point - 0.5
            interval_end = point + 0.5
            intervals.append((interval_start, interval_end))
            last_interval_end = interval_end

    return intervals

def main():
    points = [5.22, 6.1, 2.2, 2.5, 3.25,4.8]
    result = smallest_closed_intervals_greedy(points)
    print("Smallest set of unit-length closed intervals :")
    for interval in result:
        print(interval)

main()