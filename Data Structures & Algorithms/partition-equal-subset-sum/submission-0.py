class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums)
        if goal % 2 != 0:
            return False
            
        goal = goal // 2
        def dfs(goal, i):
            if goal == 0:
                return True
            if i >= len(nums) or goal < 0:
                return False
            res = dfs(goal - nums[i], i + 1) or dfs(goal, i + 1)
            return res

        return dfs(goal, 0)