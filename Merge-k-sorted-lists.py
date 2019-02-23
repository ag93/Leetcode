# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans = []
        for i in range(len(lists)):
            current = lists[i]
            while(current != None):
                ans.append(current.val)
                current = current.next
        return(sorted(ans))