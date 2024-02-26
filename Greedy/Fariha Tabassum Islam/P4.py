def min_stops(D, m, gas_stations):
    current_position = 0
    stops = []
    num_stops = 0

    for i in range(len(gas_stations)):
        if gas_stations[i] - current_position > m:
            stops.append(gas_stations[i - 1])
            current_position = gas_stations[i - 1]
            num_stops += 1

    # Check if the last gas station can be reached
    if D - current_position > m:
        stops.append(gas_stations[-1])
        num_stops += 1

    return stops, num_stops

def main():
    D = 200 
    m = 50   
    gas_stations = [50, 80, 120, 160]  # Distances of gas stations from St. Louis

    stops, num_stops = min_stops(D, m, gas_stations)
    print("Gas stations where you should stop:", stops)
    print("Number of stops required:", num_stops)
main()