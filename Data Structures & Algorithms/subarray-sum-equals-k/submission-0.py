class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        acc = 0
        prefixes = { 0: 1 }
        for n in nums:
            acc += n
            diff = acc - k
            if diff in prefixes:
                res += prefixes[diff]
            prefixes[acc] = prefixes.get(acc, 0) + 1
        return res