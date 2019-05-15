class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_nos = [num for num in A if num % 2 == 0]
        odd_nos = [num for num in A if num % 2 != 0] 
        return(even_nos+odd_nos)