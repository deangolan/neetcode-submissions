class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binSearch(target):
            l = 0
            r = len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        start = binSearch(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = binSearch(target+1) - 1

        return [start, end] 