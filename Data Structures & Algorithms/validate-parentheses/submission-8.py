class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack:
                    return False
                p = stack.pop()
                print(p)
                if close_to_open[char] != p:
                    return False

        return True if len(stack) == 0 else False

        