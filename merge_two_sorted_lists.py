# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#push nodes from l1 and l2 to list
#sort list
#add nodes to l3

#or 
#add l2 to l1 and compare to to be in order

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list = []
        
        current = l1
        while current is not None:
            list.append(current.val)
            current = current.next
        
        current = l2
        while current is not None:
            list.append(current.val)
            current = current.next
            
        list.sort()
        ListNode(list)
            
                
        
        
            
            
            