class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window (you sold on the oa when u had sliding window so lock in)
        # initialize the pointers and result for maxProfit
        l, r = 0, 1
        mP = 0

        # here the pointer has the be less than the length of the input as the window slides open(remember that)
        while r < len(prices):
            # if the future price is higher, calculate the profit and update the result
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mP = max(mP, profit)
                # then we look at other ones ahead
                r += 1
            # if not we update l to the cheapest price seen which is r and increment to our future price
            # this works as we have to sell in the future so past lowers dont matter
            else:
                l = r
                r += 1
        return mP
        