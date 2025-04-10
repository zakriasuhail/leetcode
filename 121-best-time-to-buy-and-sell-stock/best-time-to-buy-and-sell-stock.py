"""
low = 7
high = 7


low = 1
high = 1




"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit

