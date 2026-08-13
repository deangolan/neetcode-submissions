class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = { 0: 1 }

        def dp(target):
            if target < 0:
                return 0
            if target in memo:
                return memo[target]
            ans = sum(dp(target - n) for n in nums)
            memo[target] = ans
            return ans

        return dp(target)