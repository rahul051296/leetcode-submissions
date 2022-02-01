class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        stack = []
        s = list(s)
        for i, ch in enumerate(s):
            if ch is '(':
                stack.append((i, ch))
            elif ch is ')':
                if len(stack) == 0:
                    stack.append((i, ch))
                else:
                    idx, c = stack.pop()
                    if c == ')':
                        stack.append((idx, c))
                        stack.append((i, ch))
        while len(stack):
            i, curr = stack.pop()
            s.pop(i)
        return "".join(s)
        