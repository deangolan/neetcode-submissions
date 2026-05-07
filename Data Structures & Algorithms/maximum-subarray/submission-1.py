class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]

        for n in nums[1:]:
            if cur_sum > 0:
                cur_sum += n
            else:
                cur_sum = n
            max_sum = max(cur_sum, max_sum)

        return max_sum