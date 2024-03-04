def min_stops(D, m, gas_stations):
    current_position = 0
    stops = []
    num_stops = 0

    for i in range(len(gas_stations)):
        if gas_stations[i] - current_position > m:
            stops.append(gas_stations[i - 1])
            current_position = gas_stations[i - 1]
            num_stops += 1

    # Check if the destination can be reached from the last gas station
    if D - current_position > m:
        return [], -1  # Cannot reach destination
    
    return stops, num_stops


def main():
    D = 20 
    m = 10   
    gas_stations = [2, 8, 12, 14]  # Distances of gas stations from St. Louis

    stops, num_stops = min_stops(D, m, gas_stations)
    if num_stops == -1:
        print("Can't reach destination")
    else:
        print("Gas stations where you should stop:", stops)
        print("Number of stops required:", num_stops)

main()
