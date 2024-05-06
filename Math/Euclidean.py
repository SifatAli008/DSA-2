import numpy as np

P1 = (1, 1, 1, 1)
P2 = (2, 2, 2, 2)

dist_sq = 0

for i in range(len(P1)):
    dist_sq += (P1[i] - P2[i])**2

dist = np.sqrt(dist_sq)
print(dist)
