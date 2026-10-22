class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            buying_price = min(buying_price, prices[i])
            selling_price = prices[i]
            max_profit = max(selling_price - buying_price, max_profit)
        
        return max_profit
        