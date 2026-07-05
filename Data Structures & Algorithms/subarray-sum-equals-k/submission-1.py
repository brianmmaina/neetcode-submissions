class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currsum = 0
        prefixsums = {0 : 1}
        
        for num in nums:
            currsum += num
            diff = currsum - k

            res += prefixsums.get(diff, 0)
            prefixsums[currsum] = 1 + prefixsums.get(currsum, 0)

        return res
        