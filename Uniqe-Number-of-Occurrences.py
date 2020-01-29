class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        import collections
        cnt = collections.Counter(arr)
        return(len(list(cnt.values())) == len(set(cnt.values())))