# class Solution(object):
#     def minDeletionSize(self, A):
#         ans = 0
#         for col in zip(*A):
#             if any(col[i] > col[i+1] for i in xrange(len(col) - 1)):
#                 ans += 1
#         return ans



def minDeletionSize(strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        cols = []
        for i in range(len(strs[0])):
            col = ""
            for word in strs:
                col+=word[i]
            cols.append(col)

        result = 0
        for col in cols:
            if col != ''.join(sorted(col)):
                result += 1

        return result


if __name__ == "__main__":
    strs = ["zyx","wvu","tsr"]
    print(minDeletionSize(strs))