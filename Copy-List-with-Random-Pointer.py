"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        
        pointer = head
        
        while pointer:
            new_node = Node(pointer.val, None, None)
            new_node.next = pointer.next
            pointer.next = new_node
            pointer = new_node.next
        
        pointer = head
        
        while pointer:
            pointer.next.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next
            
        ptr_old_list = head
        ptr_new_list = head.next
        
        head_new = head.next
        
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
            
        return head_new