class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initialize result array
        res = []
        # sort array to perform two pointer method
        nums.sort()

        # this is the third integer that we will perform permutations on
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue

            # perform 2 sum with 3rd int
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                # if its greater than 0 we need less
                if threeSum > 0:
                    r -= 1
                # if its less than 0 we need more
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    # we only increment the left as it will do the same for the right if needed
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res