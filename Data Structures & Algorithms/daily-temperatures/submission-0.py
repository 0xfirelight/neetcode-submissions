class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > t:
                    result[i] = j-i
                    break


        return result


        