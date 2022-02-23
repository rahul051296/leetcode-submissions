# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res = set()
        
        def dfs(node):
            nonlocal res
            if not node:
                return
            res.add(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)

        if len(res) <=1:
            return -1
        return sorted(res)[1]