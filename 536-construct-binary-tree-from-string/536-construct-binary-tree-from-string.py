# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        stack =[]
        multi = 1
        for c in s:
            if not stack:
                node = TreeNode(0)
                stack.append(node)
            if c == '(':
                node = TreeNode(0)
                p = stack[-1]
                if p.left:
                    p.right = node
                else:
                    p.left = node
                stack.append(node)
                multi = 1
            elif c == ')':
                stack.pop()
            elif c == '-':
                multi = -1
            elif c.isdigit():
                node.val = node.val * 10 + multi*int(c)
        return stack.pop()