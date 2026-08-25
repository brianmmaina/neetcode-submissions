class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # here we use charSet and the sliding window, if the character is in the set, we take out the left until its not repeating
        charSet = set()
        # we initalize the l pointer and iterate with the right, fixed point on the sliding window
        l = 0
        res = 0

        for r in range(len(s)):
            #if the current character is the set, we remove it and keep doing so until its not in the set to avoid duplicates
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # once we remove all instances of it we add it and recalulate the longest lengthOfLongestSubstring
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
                
        