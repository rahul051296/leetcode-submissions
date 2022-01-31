class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = ''
        max_value = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_value = max(max_value, (i - stack[- 1]))
        return max_value
              