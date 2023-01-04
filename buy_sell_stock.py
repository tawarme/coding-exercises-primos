class Solution:
    def maxProfit(self, prices) -> int:

        profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price
        
        return profit
