class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #check length of both strings and see if they are equal or not
        if len(s1) > len(s2):
            return False

        #create a counter for both strings
        s1Count, s2Count = [0] * 26,[0] * 26

        # fill counts for all characters in s1 and s2 strings using ord method
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # count how many character frequencies match between s1 and current window of s2
        matches = 0
        for i in range(26):
            # if s1 has the same count of charcter 'i as our window, we increment it
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # left pointer for sliding window    
        l = 0

        # Right pointer expands the window to include new characters from s2
        # We start at len(s1) because we already processed the first window above

        for r in range(len(s1), len(s2)):
            # Early exit: if all 26 letters match then we found a permutation
            if matches == 26:
                return True

            # Here we add a new character. 
            # Convert it to ord and add the character to the window count
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            # Update matches:
            # If counts now match, we have one more matching character
            if s1Count[index] == s2Count[index]:
                matches += 1

            # If we just exceeded the count, we broke a match
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Here we remove an old character. 
            # Convert it to ord and add the character to the window count
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            # Update matches:
            # If counts now match, we have one more matching character
            if s1Count[index] == s2Count[index]:
                matches += 1

            # If we just exceeded the count, we broke a match
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Left pointer forward
            l += 1

        return matches == 26








            
        