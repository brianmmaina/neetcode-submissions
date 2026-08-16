class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If the substring has to be longer than s2 then it is not possible
        if len(s1) > len(s2):
            return False

        # We need to track the character frequency in S1 and a window in S2 that's size of s1
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1

        # Here, we check how many positions match between the arrays - 26 is a full match
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Here, we apply the sliding window and we start by checking if it currently matches
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # If not we add the new right character and update the count and frequency
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # We remove the left character and update the count and matches
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26
