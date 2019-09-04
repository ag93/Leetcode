class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, res = 0, 0, 0
        while left < len(s) and right < len(s):
            if s[right] not in s[left:right]:
                right += 1
            else:
                left += 1
            res = max(right - left, res)
        return res