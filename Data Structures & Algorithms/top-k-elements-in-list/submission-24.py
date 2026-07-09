class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # frequency map for each value in nums, intialize empty array
        freq = [[] for i in range(len(nums)+1)]

        # collect count of all numbers
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        # now going through the count, append the number(n) to the number of occurences(c)
        for n, c in count.items():
            freq[c].append(n)

        #iterate through results
        res = []
        for i in range(len(freq) - 1, 0, -1):
            #for each number, append the n value to the result
            for n in freq[i]:
                res.append(n)
                # when the lenght of result = k, we return result
                if len(res) == k:
                    return res

        