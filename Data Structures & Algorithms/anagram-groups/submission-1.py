class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #mapping the charcount to list of anagrams
        res = defaultdict(list)
        for s in strs:
            #one for each character a ... z
            count = [0] * 26

            #count the characters in s and map it by ascii value to the index
            for c in s:
                #maps it to 0 + 1
                count[ord(c)-ord('a')] += 1

            #we append it to a tuple since its non-mutible
            res[tuple(count)].append(s)
            
        return list(res.values())
        