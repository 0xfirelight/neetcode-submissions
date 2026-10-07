class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for i in range(len(operations)):
            op = operations[i]
            j = len(records)-1
            
            # assumes valid inputs
            if op == '+':
                records.append(records[j] + records[j-1])
            elif op == 'D':
                records.append(records[j] * 2)
            elif op == 'C':
                records.pop()
            else:
                records.append(int(op))

        print(records)
        return sum(records)
        