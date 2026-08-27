class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, h in enumerate(heights):
            while stack and stack[-1][0] <= h:
                stack.pop()
            stack.append((h, i))
        return [ i for _, i in stack ]

