# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
  None          x           y          None
             next=y     next=None       
                     
1.           next=y     next=None       
 prev_node   curr_node  next_node

Loop 1
2a.          next=y     next=None      
prev_node    curr_node  
             next_node    
                      
2b.          next=None  next=None       
prev_node    curr_node  next_node

2c.          next=None   next=x       
prev_node    curr_node    next_node

2d.          next=None   next=x       
             curr_node    next_node
             prev_node

Loop 2
  None          x           y          None
2a.          next=None     next=None      
             prev_node     curr_node
                           next_node    
                      
2b.          next=None     next=None       
             prev_node     curr_node    next_node
                        

2c.          next=None     next=x       
             prev_node     curr_node    next_node

2d.          next=None     next=x       
                           curr_node    next_node
                           prev_node


1. Before loop: 
    a. set next_node to head 
    b. set prev_node to None
2. Loop while next_node != None
    a. set curr_node to next_node
    b. set next_node to curr_node.next
    c. set curr_node.next to prev_node
    d. set prev_node to curr_node
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            
        return prev_node                
