class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        acc = 1
        l = 0
        for r, n in enumerate(nums):
            acc *= n
            while acc >= k and l < r:
                acc /= nums[l]
                l += 1
            if acc < k:
                count += r - l + 1
        return count
