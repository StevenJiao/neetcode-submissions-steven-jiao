class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]

            if (buy < sell):
                maxP = max(maxP, sell - buy)
                r += 1
            else:
                l = r
                r = r + 1
                
        return maxP