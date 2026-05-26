class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #creates a dictionary with the key(the actual number) and value(the index) 
        prev = {}

        #loop through the index and value
        for i, n in enumerate(nums):
            #calculate the difference between the target and current value
            diff = target - n

            #if the diff has been seen before, output it and the current number
            if diff in prev:
                return [prev[diff], i]

            #if not add it to the dict
            prev[n] = i


        