class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        l,r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mProfit = max(profit, mProfit)
                r += 1
            else:
                l = r
                r += 1
        return mProfit
        