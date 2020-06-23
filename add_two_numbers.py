# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#traverse through L1 and push the numbers to a stack1
#traverse through L2 and push the numbers to a stack2
#convert the numbers in both arrays to strings and join them to combine just two numbers
#the result will be the sum of the 2 numbers
#add the number, in reverse, to a LL


#('l1', ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}})


class Solution(object):
    def __init__(self, result):
        self.result = result
        
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        current = l1  
        
        #('l1', ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}})
        while current is not None:
            
            stack1.append(current.val)
            print("cu",current.val)

            
            current = l1.next
            print("cur now", current)
            l1 = current
            
        current = l2
        stack1.reverse()
        stringify = [str(num) for num in stack1]
        value1 = "".join(stringify)
        value1 = int(value1)
        print("value1", value1)
        print("STACK", stack1)
        
        
        #('l2', ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}})
        while current is not None:
            print("L2", l2)
            stack2.append(current.val)
            print("cu",current.val)

            
            current = l2.next
            print("cur now", current)
            l2 = current
            
        stack2.reverse()
        stringify = [str(num) for num in stack2]
        value2 = "".join(stringify)
        value2 = int(value2)
        print("value2", value2)
        print("STACK", stack2)
        
        
        self.result = value1 + value2
        
        