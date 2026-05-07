class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_n = nums[0]
        for n in nums[1:]:
            if n < min_n:
                return n
        return min_n