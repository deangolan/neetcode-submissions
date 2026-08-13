class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(goal):
            res = 0

            l = 0
            cur = 0
            for r, n in enumerate(nums):
                cur += n
                while l < r and cur > goal:
                    cur -= nums[l]
                    l += 1
                if cur <= goal:
                    res += r - l + 1

            return res

        return helper(goal) - helper(goal-1) if goal > 0 else helper(goal)