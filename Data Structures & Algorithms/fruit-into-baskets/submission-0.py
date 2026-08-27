class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        freqs = defaultdict(int)
        res = 0
        for r, fruit in enumerate(fruits):
            freqs[fruit] += 1
            while len(freqs) > 2:
                lf = fruits[l]
                if freqs[lf] == 1:
                    freqs.pop(lf)
                else:
                    freqs[lf] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res