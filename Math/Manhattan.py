
def get_Manhattan_distance(P1, P2):
    distance = 0

    for i in range(len(P1)):
        distance += abs(P1[i] - P2[i])

    return distance

def main():
    P1 = (1, 1, 1, 1)
    P2 = (2, 2, 2, 2)
    distance = get_Manhattan_distance(P1, P2)
    print("Manhattan distance:", distance)

main()
