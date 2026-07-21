class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        counters = {
            '(': 0,
            '{': 0,
            '[': 0
            }
        
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }


        stack = []


        for char in s: 
            # is opening
            if char == '(' or char == '{' or char == '[': 
                stack.append(char)
                continue
            # is closing 
            if len(stack) == 0:
                # ran out of opening parens?
                return False
            prev = stack.pop()
            opening = close_to_open[char]
            if prev != opening:
                return False
        
        if len(stack) > 0:
            return False
        return True
        