import math

def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

points = [(1, 2), (3, 4), (-5, 12), (7, -1)]

point_A = points[0]
point_B = points[1]
dist = get_distance(point_A, point_B)

print("Distance between", point_A, "and", point_B, "is:", dist)

origin = (0, 0)
farthest_point = points[0]
max_dist = get_distance(points[0], origin)

for p in points:
    d = get_distance(p, origin)
    if d > max_dist:
        max_dist = d
        farthest_point = p

print("Farthest point from (0,0) is:", farthest_point)