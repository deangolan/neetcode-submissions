class Solution:

    def __init__(self, w: List[int]):
        self.nums = [i for i, n in enumerate(w) for _ in range(n)]

    def pickIndex(self) -> int:
        return self.nums[random.randint(0, len(self.nums)-1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()