class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        startWordSet = set()

        for word in startWords:

            h = 0
            for ch in word:
                h ^= 1 << (ord(ch) - ord('a'))

            startWordSet.add(h)

        ret = 0
        for i in range(len(targetWords)):

            h = 0
            for ch in targetWords[i]:
                h ^= 1 << (ord(ch) - ord('a'))

            for ch in targetWords[i]:

                rh = h ^ (1 << (ord(ch) - ord('a')))

                if rh in startWordSet:
                    ret = ret + 1
                    break

        return ret







