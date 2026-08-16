class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, the shortest window is empty
        if t == "":
            return ""

        # countT: frequency of characters we NEED in t
        # window: frequency of characters CURRENTLY in our sliding window
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have: how many unique characters we've satisfied (have exactly enough of)
        # need: how many unique characters we need to satisfy (just unique chars in t)
        have, need = 0, len(countT)
        
        # res: store [left, right] indices of the best window found so far
        # resLen: length of the best window found so far (initially infinity)
        res, resLen = [-1, -1], float("infinity")
        
        # l: left pointer of sliding window
        l = 0
        
        # Expand the right pointer one character at a time
        for r in range(len(s)):
            c = s[r]
            # Add the new character to our window frequency count
            window[c] = 1 + window.get(c, 0)

            # If this character is in t AND we now have exactly the required amount,
            # then we've satisfied one more unique character
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # While we have satisfied ALL required characters,
            # try shrinking the window from the left to find a smaller valid window
            while have == need:
                # Update result if this window is smaller than the best so far
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Remove the leftmost character from window
                window[s[l]] -= 1
                
                # If removing this character makes us no longer satisfy t,
                # decrease our "have" counter
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                # Move left pointer right to shrink the window
                l += 1

        # Extract the result substring
        l, r = res
        # If resLen is still infinity, no valid window was found
        return s[l : r + 1] if resLen != float("infinity") else ""