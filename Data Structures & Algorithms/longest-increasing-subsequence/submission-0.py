class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [9,8,10]
        #    9
        #   /\
        #  
        # [9,1,1]
        out = [1]
        memo = { len(nums): 1 }
        def dfs(i):
            if i in memo:
                return memo[i]
            res = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    res = max(res, dfs(j)+1)
            out[0] = max(res, out[0])
            memo[i] = res
            return res

        for i in range(len(nums)-1, -1, -1):
            dfs(i)

        return out[0]