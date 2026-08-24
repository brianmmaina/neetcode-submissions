class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since the array is sorted, we can use two pointers from either side
        l, r = 0, len(numbers) - 1
        while l < r:
            # if the number is smaller than the target, we increment the left pointer to increase the sum
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            # we return the index + 1 if its the target as its sorted and theres a -1 delay with indexes
            else:
                return[l + 1, r + 1]
        