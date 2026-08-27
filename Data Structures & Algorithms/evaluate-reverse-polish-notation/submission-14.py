class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <= 1:
            return int(tokens[0])

        ops = {'*', '-', '/', '+'}
        stack = []

        for t in tokens:
            if t in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                res = self.perform_op(int(op1), int(op2), t)
                stack.append(res)
            else:
                stack.append(t)

        if len(stack) != 1:
            raise 'Crap'

        return int(stack[0])


    def perform_op(self, operand1, operand2, op):
        if op == '*':
            return operand1 * operand2
        if op == '+':
            return operand1 + operand2
        if op == '/':
            return operand1 / operand2
        if op == '-':
            return operand1 - operand2


        