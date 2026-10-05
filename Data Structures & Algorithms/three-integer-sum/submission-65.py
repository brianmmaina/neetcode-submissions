class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initalize result and sort the List
        res = []
        nums.sort()

        # we have to iterate through the loop while focusing on one integer relative to the other two
        for i, a in enumerate(nums):

            #if a is greater than 0, we break
            if a > 0:
                break
            
            #if our index is greater than 0 and our previous number is the same as our current we continue
            if i > 0 and a == nums[i -1]:
                continue

            # we initalize our pointers to be ahead of i and we do the two sum as if it was sorted
            l, r = i + 1, len(nums) - 1
            while l < r:
                #  compute the 3sum
                threesum = a + nums[l] + nums[r]
                # if the threesum is greater than 0, we have to decrement our r so we end up closer to 0 vice versa
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # we only increment l as it allows us to look at all the combinations
                    l += 1

                    # if the current nums[l] == nums[l -1], we increment again to avoid duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
