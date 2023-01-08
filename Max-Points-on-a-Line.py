# Make Leetcode Happy Solution
# n = len(points)
#         if n == 1:
#             return 1
#         result = 2
#         for i in range(n):
#             cnt = collections.defaultdict(int)
#             for j in range(n):
#                 if j != i:
#                     cnt[math.atan2(points[j][1] - points[i][1],
#                                    points[j][0] - points[i][0])] += 1
#             result = max(result, max(cnt.values()) + 1)
#         return result

# More Probable solution
import collections
def calLine(x1, y1, x2, y2):    # calculate the line equation
    if x1 == x2:
        return (1, 0, -x1)
    m = (y1 - y2) / (x1 - x2)   # Calculate slope m
    c = y1 - m * x1             # y = mx + c, therefore c = y - mx
    return (m, -1 ,c)

def maxPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    n = len(points)
    if n == 1:
        return 1

    res = 0
    for i in range(n):
        mem = collections.defaultdict(set)
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            line = calLine(x1, y1, x2, y2)
            mem[line].add((x1, y1))
            mem[line].add((x2, y2))
            res = max(res, len(mem[line]))
    return res

if __name__ == "__main__":
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(maxPoints(points))
