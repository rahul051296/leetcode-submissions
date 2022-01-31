# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            pivot = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[pivot])
            root.left = self.buildTree(preorder, inorder[0:pivot])
            root.right = self.buildTree(preorder, inorder[pivot+1:])
        
            
            return root
            
            