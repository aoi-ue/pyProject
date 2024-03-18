from typing import List


class SlidingWindow:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for selling in prices:
            if selling < lowest:
                lowest = selling
            profit = max(profit, selling - lowest)
        return profit
