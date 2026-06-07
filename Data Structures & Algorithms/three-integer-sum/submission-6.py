class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and n == nums[i-1]:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                total = n + nums[L] + nums[R]

                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                else:
                    res.append([n, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L -1]:
                        L += 1
        return res

            
        