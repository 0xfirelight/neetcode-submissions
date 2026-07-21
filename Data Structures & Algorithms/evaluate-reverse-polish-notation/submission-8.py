import re

class Solution:
    def is_operator(self, token) -> bool:
        if token == '+':
            return True
        if token == '-':
            return True
        if token == '*':
            return True
        if token == '/':
            return True
        return False

    def do_operation(self, operator, operand1, operand2):
        match operator:
            case '+':
                return operand1 + operand2
            case '-':
                return operand1 - operand2
            case '*':
                return operand1 * operand2
            case '/':
                return int(operand1 / operand2)
            

    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]
        idx = 1

        op_result = None

        while idx < len(tokens):
            el = tokens[idx]
            idx += 1
            if not self.is_operator(el):
                stack.append(int(el))
                continue

            op_result = stack.pop()
            operand2 = stack.pop()
            op_result = self.do_operation(el, operand2, op_result)

            stack.append(op_result)
            print(stack)

        return stack[0]
        