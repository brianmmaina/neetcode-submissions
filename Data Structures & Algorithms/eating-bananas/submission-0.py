class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum and maximum possible bananas per hour
        l, r = 1, max(piles)
        res = r

        # we check the middle and we do left or right
        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            # Compute the total hours needed using this speed.
            for p in piles:
                totalTime += math.ceil((p) / k)
            # if we can do it under the threshold we check the left side
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            # if we cant we check the right side
            else:
                l = k + 1
        return res

        