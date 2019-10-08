class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, i):
            if i == len(s) // 2:
                return
            reverse(s, i+1)
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
			
        reverse(s, 0)