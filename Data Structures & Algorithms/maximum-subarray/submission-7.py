class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        acc = nums[0]

        for n in nums[1:]:
            if acc < 0:
                acc = 0
            acc += n
            curMax = max(curMax, acc)
        
        return curMax