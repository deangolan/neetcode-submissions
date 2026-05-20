class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref = { 0: -1 }
        acc = 0
        res = 0
        for i, n in enumerate(nums):
            acc += n
            r = acc % k
            if r in pref:
                if i - pref[r] >= 2:
                    return True
            else:
                pref[r] = i
        return False
