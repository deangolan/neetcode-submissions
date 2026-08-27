class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        potential = [0] * n
        satisfied = 0
        for i, c in enumerate(customers):
            if grumpy[i] == 1:
                potential[i] = c
            else:
                satisfied += c
                
        r = minutes
        wind = sum(potential[0:r])
        res = satisfied + wind
        while r < n:
            wind = wind - potential[r-minutes] + potential[r]
            res = max(satisfied + wind, res)
            r += 1
        return res