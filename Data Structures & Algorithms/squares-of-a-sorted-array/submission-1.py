class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # have to build it in reverse order
        # initalize pointers and result array
        l, r, res = 0, len(nums) - 1, []

        # append the larger number when squared
        while l <= r:
            # when nums[l] squared is larger
            if (nums[l] * nums[l]) > (nums[r] * nums[r]):
                res.append(nums[l] * nums[l])
                l += 1
            # when nums[r] squared is larger 
            else:
                res.append(nums[r] * nums[r])
                r -= 1
        return res[::-1] # reverse the array


        