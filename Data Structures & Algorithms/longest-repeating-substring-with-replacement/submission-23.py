class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # intialize frequency map so we can store the frequency of characters
        count = {}

        # intialize maxf, l pointer and the result
        maxF = 0
        res = 0
        l = 0

        # using the right pointer update the frequency of s[r] and update maxF
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

        # if the current window size - the max frequency is greater than k, we decrease the window:
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            