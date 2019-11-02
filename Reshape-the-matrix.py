class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = [i for row in nums for i in row]
        if r*c == len(flatten):
            return [flatten[i*c : (i+1)*c] for i in range(r)]
        else:
            return nums