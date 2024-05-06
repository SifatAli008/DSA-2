import numpy as np

def get_eulidean_distance(P1, P2):
    dist_sq = 0

    for i in range(len(P1)):
        dist_sq += (P1[i] - P2[i])**2

    dist = np.sqrt(dist_sq)
    return dist

def main():
    P1 = (1, 1, 1, 1)
    P2 = (2, 2, 2, 2)
    distance = get_eulidean_distance(P1, P2)
    print("Euclidean distance:", distance)

main()