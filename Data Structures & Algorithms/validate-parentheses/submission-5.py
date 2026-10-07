class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        close_to_open = {')': '(', '}': '{', ']': '['}

        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                    
                op = stack.pop()
                if close_to_open[c] != op:
                    return False


        return len(stack) == 0

        