class Solution(object):
    def maxProfit(self, prices):
        max_price = 0
        min_price = float("inf")
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_price:
                max_price = price - min_price
        return max_price
