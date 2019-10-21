# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        dummyhead = ListNode(0)
        curr = dummyhead
        carry = 0
        
        while(p != None or q != None):
            if p != None:
                x = p.val
            else:
                x = 0
            
            if q != None:
                y = q.val
            else:
                y = 0
                
            summ = x + y + carry
            carry = summ//10
            
            curr.next = ListNode(summ%10)
            curr = curr.next
            
            if (p!= None):
                p = p.next
                
            if (q!= None):
                q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry)
            
        return dummyhead.next