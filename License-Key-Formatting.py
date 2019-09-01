class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()
        right = len(S)- K
        while(right > 0):
            S = S[:right] + "-" + S[right:]
            right = right-K
        return(S)