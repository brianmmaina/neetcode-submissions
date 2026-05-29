class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store how many times each number appears
        count = {}

        # Count the frequency of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Create a list of [frequency, number] pairs
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        # Sort the list so the least frequent numbers come first
        # and the most frequent numbers come last
        arr.sort()

        # Result list for the top k frequent numbers
        res = []

        # Pop from the end because the most frequent items are at the end
        while len(res) < k:
            res.append(arr.pop()[1])  # only add the number, not the frequency

        return res