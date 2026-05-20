class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur = 0
        res = float('inf')
        for r, n in enumerate(nums):
            cur += n
            while cur >= target and l <= r:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0
