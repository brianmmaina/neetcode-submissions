class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mprofit = 0
        l,r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mprofit = max(mprofit, profit)
                r += 1
            else:
                l = r
                r += 1
        return mprofit
        