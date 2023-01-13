import collections
class Solution:
    def longestPath(self, parent, s):
        tree = collections.defaultdict(list)
        for end,start in enumerate(parent):
            tree[start].append(end)
        res = 1

        def dfs(node):
            nonlocal res
            max1 = max2 = 0

            for nei in tree[node]:
                neiL = dfs(nei)
                # This condition makes sure the path is valid.
                if s[nei] != s[node]:
                    # Update the length of the top two longest paths.
                    if neiL > max1:
                        max2 = max1
                        max1 = neiL
                    elif neiL > max2:
                        max2 = neiL
            res = max(res, max1+max2+1)
            return max1+1
        
        dfs(0)
        return res