class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            if i == n:
                return 1
            if i > n:
                return 0

            one = dfs(i+1)
            two = dfs(i+2)
            cache[i+1] = one
            cache[i+2] = two
            return one + two
        
        return dfs(0)