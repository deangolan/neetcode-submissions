class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        potential = [0] * n
        satisfied = [0] * n
        for i, c in enumerate(customers):
            if grumpy[i] == 1:
                potential[i] = c
            else:
                satisfied[i] = c
        sat = sum(satisfied)
        res = 0
        r = minutes
        while r <= n:
            wind = sum(potential[r-minutes:r])
            res = max(sat + wind, res)
            r += 1
        return res