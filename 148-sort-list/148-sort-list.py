# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.getMid(head)
    
        l = self.sortList(head)
        r = self.sortList(mid)
        
        if not l or not r:
            return l or r
        temp = ListNode(0)
        curr = temp
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        curr.next = l or r
        return temp.next
       
        
    
    def getMid(self,node):
        slow = node
        fast = node.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next   
        slow.next = None
        return start
