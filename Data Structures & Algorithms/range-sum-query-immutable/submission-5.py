class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixes = [0] * (len(nums) + 1)
        self.prefixes[0] = nums[0]
        for i in range(len(nums)):
            self.prefixes[i+1] = self.prefixes[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixes[right+1] - self.prefixes[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)