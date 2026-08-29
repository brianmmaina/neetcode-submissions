class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxF = 0
        l = 0
        longest = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count.get(s[r]))
        
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

        
        