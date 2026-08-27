class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = 0
        prev = 0
        for n in target:
            if prev < n:
                ops += n - prev
            prev = n
        return ops
