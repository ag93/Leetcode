total_crates = 6
points = [[3,6], [2,4], [5,3], [2,7], [1,8], [7,9]]
K = 3

points.sort(key = lambda P: P[0]**2 + P[1]**2)
print(points[:K])