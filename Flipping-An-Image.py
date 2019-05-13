class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in range(0, len(A)):
            A[row] = list(reversed(A[row]))
            A[row] = [0 if x==1 else 1 for x in A[row]]
        return(A)