class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        zeros = 0
        l = 0
        for r, n in enumerate(nums):
            if n == 0:
                zeros += 1
            while zeros > k and l < r: 
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                res = max(res, r - l + 1)
        return res
