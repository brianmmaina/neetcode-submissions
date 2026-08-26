class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonically decreasing queue

        # initalize output array, queue and maxSlidingWindow
        output = []
        q = deque()
        l = r = 0

        # we run it until the right pointer is not in bound
        while r < len(nums):
            # we have to check and make sure no smaller values are in the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # if the left value is out of bounds, we remove it from the the window
            if l > q[0]:
                q.popleft()

        
            # edge case, gotta make sure the window is atleast size k before adding the max of the window to the output    
            if (r + 1) >= k:
                output.append(nums[q[0]])
                # left pointer is only incremented when we hit the max window size
                l += 1
            r += 1
        return output

        