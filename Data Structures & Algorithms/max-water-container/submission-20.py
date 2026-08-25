class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initalize pointers and max area variable
        mA = 0
        l, r = 0, len(heights) - 1
        while l < r:
            # calculate the area and update the maximum
            area = min(heights[l], heights[r]) * (r - l)
            mA = max(mA, area)
            # if the height l is equal or smaller than the right, we move up the left pointer, else we move the right
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        # this way we check the best combos and actually work on improving our maxArea
        return mA
        