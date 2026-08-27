class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixes = [0] * len(nums)
        self.prefixes[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefixes[i] = self.prefixes[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixes[right]
        return self.prefixes[right] - self.prefixes[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)