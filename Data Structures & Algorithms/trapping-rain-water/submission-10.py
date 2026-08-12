class Solution:
    def trap(self, height: List[int]) -> int:
        #base case for no trapped water
        if not height:
            return 0

        # so we set two pointers, and then we intialize the tallest walls seens so far
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        res = 0
        #here we do the comparisons to get the tallest walls for the left and right and add the  difference to out total
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
        return res
        