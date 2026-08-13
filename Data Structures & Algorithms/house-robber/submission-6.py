class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]

        dp = [0] * N
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-2:])
        for i in range(N-3, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        return dp[0]