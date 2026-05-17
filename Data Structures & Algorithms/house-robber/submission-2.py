class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums = [2,9,8,3,6]
        # rob 6, 8, 2 -> 16
        # nums = [2,9,8,100,6]
        # nums = [2,109,100,100,6]
        # rob 100, 9 -> 109
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i+1], nums[i] + nums[i+2])
        return max(nums[0], nums[1])