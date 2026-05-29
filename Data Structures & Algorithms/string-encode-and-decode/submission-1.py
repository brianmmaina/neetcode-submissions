class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # find the delimiter after the length
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # actual string starts after #
            start = j + 1
            word = s[start:start + length]

            result.append(word)

            # move i to the next encoded segment
            i = start + length

        return result
