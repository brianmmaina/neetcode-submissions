class Solution:
    def trap(self, height: List[int]) -> int:
        # initalize pointers, results for trapped water, and tallest heights seen
        l, r = 0, len(height) - 1
        res = 0
        leftmax, rightmax = height[l], height[r]

        while l < r:
            # if the height of the left max is less than the right max, we increment our left and check for trapped water
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            # we repeat the same procress for the right until they both meet that way we cover all the trapped water
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
        # proof read your code for small errors when copy pasting repeated sections buddy
        return res
        