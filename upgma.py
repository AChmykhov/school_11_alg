import numpy as np


class Cluster:
    def __init__(self, coords=np.array([]), weight=1, child_1=None, child_2=None):
        if child_2 is None:
            self.coord = coords
            self.weight = weight
            self.childs = [None, None]
        else:
            k = child_1.weight / (child_1.weight + child_2.weight)
            self.coord = child_1.coord * k + child_2.coord * (1 - k)
            self.weight = child_1.weight + child_2.weight
            self.childs = [child_1, child_2]

    def distance(self, point):
        return np.linalg.norm(self.coord - point.coord)

    def __str__(self):
        return f"[coords {str(self.coord)}, weight = {str(self.weight)}]"

    def __repr__(self):
        return f"[coords {str(self.coord)}, weight = {str(self.weight)}]"


# points array
A_points = [[21, 3], [20, 4], [22, 2], [0, 0], [-10, 0], [-10, 1], [-9, -1], [100, 50], [110, 40], [95, 60],
            [105, 70]]

# create array of clusters

A = [Cluster(coords=np.array(i)) for i in A_points]
print(A, len(A))
while len(A) > 1:
    min_d = np.inf
    a, b = None, None
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            distance = A[i].distance(A[j])
            if min_d > distance:
                min_d = distance
                a, b = i, j

    A.append(Cluster(child_1=A[a], child_2=A[b]))
    A.pop(b)
    A.pop(a)
    print(str(A))
