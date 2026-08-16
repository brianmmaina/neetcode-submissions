class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        # Using deque, we can store indicies of elements ind ecreasing order of their values
        q = deque()
        l = r = 0

        # Expand the window by moving the right pointer
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                # Before inserting r, remove indices whose values are smaller than the new value 
                q.pop()
            # Here, we add the new index to deque
            q.append(r)

            # If the left pointer passes the front index, remove it (it's outside the window).
            if l > q[0]:
                q.popleft()

            # Once the window reaches size k, the front of the deque represents the maximum.
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
        