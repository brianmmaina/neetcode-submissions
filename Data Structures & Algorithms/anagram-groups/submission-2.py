class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This dictionary will store groups of anagrams.
        # The key is a pattern that represents the letters in the word.
        # The value is a list of words that match that pattern.
        groups = defaultdict(list)

        # Go through every word in the input list
        for word in strs:
            # Make a list of 26 zeros, one for each letter a-z
            count = [0] * 26

            # Count how many times each letter appears in the word
            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            # Convert the list into a tuple so it can be used as a dictionary key
            # Words with the same letter counts are anagrams
            groups[tuple(count)].append(word)

        # Return all the groups of anagrams
        return list(groups.values())