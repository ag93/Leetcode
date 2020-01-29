class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        left = 0
        right = len(S)-1

        while left<right:
            if not S[left].isalpha():
                left += 1

            elif not S[right].isalpha():
                right -= 1

            else:    
                S[left], S[right] = S[right], S[left]
                left +=1
                right -=1
        result = "".join(S)
        return result