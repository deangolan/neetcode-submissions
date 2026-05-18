class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums)
        if goal % 2 != 0:
            return False
            
        memo = [[-1] * (goal+1) for _ in range(len(nums))]
        goal = goal // 2
        def dfs(goal, i):
            if goal == 0:
                return True
            if i >= len(nums) or goal < 0:
                return False
            if memo[i][goal] != -1:
                return memo[i][goal] 
            res = dfs(goal - nums[i], i + 1) or dfs(goal, i + 1)
            memo[i][goal] = res
            return res

        return dfs(goal, 0)