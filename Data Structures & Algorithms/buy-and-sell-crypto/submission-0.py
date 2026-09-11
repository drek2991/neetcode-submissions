class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = 101
        for price in prices:
            profit = price-buy
            if profit > best: best = profit
            if price < buy: buy = price
        return best
