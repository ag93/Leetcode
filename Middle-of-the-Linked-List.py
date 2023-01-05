# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        single_hopper = head
        double_hopper = head

        while double_hopper and double_hopper.next:
            single_hopper = single_hopper.next
            double_hopper = double_hopper.next.next

        return single_hopper