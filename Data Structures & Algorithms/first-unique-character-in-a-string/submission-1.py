class Solution:
    def firstUniqChar(self, s: str) -> int:
        # create a hashmap to store the count of each character
        count = defaultdict(int)

        # iterate through the string and increment the count for each character
        for c in s:
            count[c] += 1

        # Iterate through the string again and return the index of the character where the count == 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
        