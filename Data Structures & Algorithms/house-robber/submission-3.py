class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        one = nums[-2]
        two = nums[-1]
        for i in range(len(nums) - 3, -1, -1):
            one, two = max(nums[i] + two, one), one
        return max(one, two)