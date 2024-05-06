import numpy as np

def get_eulidean_distance(P1, P2):
    if len(P1) != len(P2):
        raise ValueError("Points must have the same number of dimensions")

    if len(P1) == 1:
        return abs(P1[0] - P2[0])

    mid = len(P1) // 2
    left_distance = get_eulidean_distance(P1[:mid], P2[:mid])
    right_distance = get_eulidean_distance(P1[mid:], P2[mid:])

    return np.sqrt(left_distance**2 + right_distance**2)

def main():
    P1 = (1, 5, 1, 0)
    P2 = (2, 1, 7, 2)
    distance = get_eulidean_distance(P1, P2)
    print("Euclidean distance:", distance)


main()
