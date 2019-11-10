class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct = sorted(heights)
        cnt = 0
        for index in range(len(heights)):
            if heights[index] != correct[index]:
                cnt += 1
        return cnt