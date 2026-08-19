# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
edge cases
one list is empty -> solved in logic since it will happen in the end
both lists are empty -> immediately return none

Set the head that will be returned 
    Lets make it list1 head val unless list2 head val is smaller
    if head is list1 curr_1 to list1.next 
    else set curr_2 to list2.next

Set a variable for the current node to curr and set it equal to head.next

do logic in while loop while curr_1 or curr_2 are valid
    None throws errors on comparisons so account for this
    works because if not both then loop isnt running
        if not curr_1  
            curr.next = curr_2 
            curr_2 = curr_2.next
        elif not curr_2 
            curr.next = curr_1 
            curr_1 = curr_1.next
        elif curr_1 val <= to curr_2 val
            curr.next = curr_1
            curr_1 = curr_1.next
        else
            curr.next = curr_2
            curr_2 = curr_2.next

'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = list1
        curr_2 = list2
        if not curr_1 or not curr_2:
            if not curr_1 and not curr_2:
                return None
            elif not curr_1:
                head = list2
                curr_2 = head.next
            elif not curr_2:
                head = list1
                curr_1 = head.next
        elif (list1.val <= list2.val):
            head = list1
            curr_1 = head.next
        else:
            head = list2
            curr_2 = head.next
            
        curr = head

        
        while curr_1 or curr_2:
            if not curr_1:
                curr.next = curr_2 
                curr = curr_2
                curr_2 = curr_2.next
            elif not curr_2:
                curr.next = curr_1 
                curr = curr_1
                curr_1 = curr_1.next
            elif curr_1.val <= curr_2.val:
                curr.next = curr_1
                curr = curr_1
                curr_1 = curr_1.next
            else:
                curr.next = curr_2
                curr = curr_2
                curr_2 = curr_2.next


        return head

