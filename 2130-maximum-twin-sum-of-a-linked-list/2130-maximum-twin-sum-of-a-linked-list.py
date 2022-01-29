# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        size = len(stack)
        max_sum = 0
        while len(stack) > size//2:
            last = stack.pop()
            first = curr.val
            max_sum = max(first+last, max_sum)
            curr = curr.next
        
        return max_sum
        
        