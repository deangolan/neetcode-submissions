class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if m == 0 or m == len(nums) - 1:
                return nums[m]
            elif nums[m] == nums[m-1]:
                if m % 2 == 0:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] == nums[m+1]:
                if m % 2 == 0:
                    l = m + 1
                else:
                    r = m - 1
            else:
                return nums[m]
        return nums[0]