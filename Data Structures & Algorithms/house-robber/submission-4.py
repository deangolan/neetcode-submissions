class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return max(nums)

        memo = { N-1: nums[-1], N-2: max(nums[-2:]) }

        def dp(i):
            if i in memo:
                return memo[i]
            ans = max(nums[i] + dp(i+2), dp(i+1))
            memo[i] = ans
            return ans

        return dp(0)