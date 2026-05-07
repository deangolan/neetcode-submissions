class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        total = 0

        curSum = 0
        curMin = 0
        for n in nums:
            total += n

            curMin += n
            minSum = min(minSum, curMin)
            curMin = min(0, curMin)

            curSum += n
            maxSum = max(maxSum, curSum)
            curSum = max(0, curSum)

        if minSum == total:
            return maxSum
        return max(maxSum, total-minSum)