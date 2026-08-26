class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case, if the string t is empty
        if t == "":
            return ""

        # two windows of count t and the empty window
        countT, window = {}, {}
        # initalize the count t map as it never changes
        res, resLen = [-1, -1], float("infinity")
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have and need concept
        have, need = 0, len(countT)
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of the window
                char_l = s[l]
                window[char_l] -= 1
                if char_l in countT and window[char_l] < countT[char_l]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""