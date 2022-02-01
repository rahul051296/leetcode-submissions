class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_start = float("inf")
        max_profit = 0
        for i, price in enumerate(prices):
            min_start = min(min_start, price)
            profit = price - min_start
            max_profit = max(profit, max_profit)
        return max_profit