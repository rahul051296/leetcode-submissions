# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        hashmap = defaultdict(int)
        
        curr = head 
        while curr:
            hashmap[curr.val] += 1
            curr = curr.next
        head = ListNode()
        curr = head
        
        for k, v in hashmap.items():
            if v == 1:
                curr.next = ListNode(k)
                curr = curr.next
        return head.next
                
            