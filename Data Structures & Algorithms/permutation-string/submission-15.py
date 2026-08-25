class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case where the substring is longer than the string
        if len(s1) > len(s2):
            return False  

        # we are implementing the hashmaps with arrays
        s1count, s2count = [0] * 26, [0] * 26

        # we have to go through all the characters of s1 and intialize both hashmaps so the windows are the same length
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord("a")] += 1
            s2count[ord(s2[i]) - ord("a")] += 1

        # we have to initalize the number of matches and iterate through the arrays and check the current matches, if the match to 26 then we have found the substring s1 in s2
        matches = 0
        for i in range(26):
            matches += 1 if s1count[i] == s2count[i] else 0

        # initalize the pointers
        l = 0
        for r in range(len(s1), len(s2)):
            # if the condition is met return true
            if matches == 26:
                return True

            # here we calculate the index and increment the count
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            # if it was previously correct then we dont need to change it and we actually decrement it
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1

            # here we calculate the index and increment the count
            # we do the opposite for left
            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            # if it was previously correct then we dont need to change it and we actually decrement it
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l += 1
        return matches == 26
