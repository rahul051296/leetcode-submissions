# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next
        left = 0
        right = len(l) - 1
        curr = head
        for i in range(right+1):
            if i % 2 != 0:
                curr.val = l[right]
                right -= 1
            else:
                curr.val = l[left]
                left += 1
            curr = curr.next
            
