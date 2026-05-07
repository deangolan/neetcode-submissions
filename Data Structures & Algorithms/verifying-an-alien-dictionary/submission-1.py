class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}
        for n, char in enumerate(order):
            mapping[char] = n

        i = 0
        j = 1
        while j < len(words):
            w1 = words[i]
            w2 = words[j]

            k = 0
            while k < len(w1) and k < len(w2):
                if mapping[w1[k]] < mapping[w2[k]]:
                    break
                if mapping[w1[k]] > mapping[w2[k]]:
                    return False
                k += 1
            if k < len(w1) and w1[0:k] == w2:
                return False

            i += 1
            j += 1

        return True