class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    # initialize max area and stack and also variable for length of input
        n = len(heights)
        maxArea = 0
        stack = []


    # iterate through the list 0 to n inclusive
        for i in range(n + 1):
    # while the stack is not empty and either we are past the last bar or the height[i] is less than or equal to the height at the top of the index
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                # pop the top index, let height be h
                height = heights[stack.pop()]
                # compute width
                width = i if not stack else i - stack[-1] -1
                # update max area
                maxArea = max(maxArea, height * width)
            # push current index onto stack
            stack.append(i)
        # return max area
        return maxArea
    
        