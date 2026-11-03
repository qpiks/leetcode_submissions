# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        prevl = dummy
        for _ in range(1, left):
            prevl = prevl.next
        
        curr = prevl.next
        for _ in range(left, right):
            temp = curr.next
            curr.next = temp.next
            temp.next = prevl.next
            prevl.next = temp
        return dummy.next


    


                
            
