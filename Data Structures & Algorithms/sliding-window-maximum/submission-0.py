class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        l = 0
        r = k
        while r <= len(nums):
            # naive
            cur_max = max(nums[l:r])
            res.append(cur_max)
            
            r += 1
            l += 1

        return res