class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        curMax = nums[0]
        curMin = nums[0]
        res = float('-inf')
        for n in nums[1:]:
            nMax = n * curMax
            nMin = n * curMin
            curMax = max(nMax, nMin, n)
            curMin = min(nMax, nMin, n)
            res = max(res, curMax)

        return res