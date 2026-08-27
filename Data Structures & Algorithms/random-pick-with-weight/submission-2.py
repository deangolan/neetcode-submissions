class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        for i, n in enumerate(w):
            self.arr += [i] * n


    def pickIndex(self) -> int:
        i = random.randint(0, len(self.arr) - 1)
        return self.arr[i]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()