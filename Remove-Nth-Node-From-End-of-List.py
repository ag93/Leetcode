# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(0, n+1):
            first = first.next
            
        while (first != None):
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next


    #-------------------------------------------------------------------
        # dummy = ListNode(-1)
        # dummy.next = head
        # linkedListLength = 0

        # pointer = head
        # while(pointer.next):
        #     linkedListLength += 1
        #     pointer = pointer.next

        # length = linkedListLength-n+1
        # first = dummy
        # while(length > 0):
        #     first = first.next
        #     length -= 1
        
        # first.next = first.next.next

        # return dummy.next