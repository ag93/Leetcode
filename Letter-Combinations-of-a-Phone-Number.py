class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': "abc",
                 '3': "def",
                 '4': "ghi",
                 '5': "jkl",
                 '6': "mno",
                 '7': "pqrs",
                 '8': "tuv",
                 '9': "wxyz"}

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        output = []
        if digits:
            backtrack("", digits)
        return(output)