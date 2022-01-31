# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(n):
            if not n:
                return None
            root_elem = max(n)
            root = TreeNode(root_elem)
            mid = n.index(root_elem)
            root.left = construct(n[:mid])
            root.right = construct(n[mid+1:])
            return root
        root = construct(nums)
        return root
        
            