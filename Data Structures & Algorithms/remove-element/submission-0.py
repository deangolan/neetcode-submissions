class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        move = 0
        k = 0
        for i, n in enumerate(nums):
            if n == val:
                move += 1
            else:
                k += 1
                nums[i - move] = n
        return k