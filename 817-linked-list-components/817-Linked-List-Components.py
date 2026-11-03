# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        seen = set(nums)

        right = head
        flag = False
        ans = 0
        while right:
            
            if right.val in seen and not flag:
                flag = True
            elif right.val not in seen and flag:
                flag = False
                ans += 1
            right = right.next
        if flag:
            ans += 1
        return ans



        # # the max length
        # left = right = head
        # ans = 0
        # length = 0
        # while right:
        #     if right.val in seen:
        #         length += 1
        #         ans = max(ans, length)
        #         right = right.next
        #     else:
        #         right = right.next
        #         left = right
        #         length = 0
        # return ans
