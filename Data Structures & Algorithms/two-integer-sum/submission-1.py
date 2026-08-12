class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we map each value to its index in the array to the hashmap
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return

        