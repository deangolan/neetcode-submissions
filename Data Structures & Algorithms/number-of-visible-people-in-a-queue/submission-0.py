class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n

        people = [heights[-1]]
        for i in range(n-2, -1, -1):
            seen = 0
            while people and people[-1] < heights[i]:
                seen += 1
                people.pop()
            if people:
                seen += 1
            res[i] = seen
            people.append(heights[i])

        return res
