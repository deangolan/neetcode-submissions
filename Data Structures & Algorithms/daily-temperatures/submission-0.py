class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 

        stack = []
        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                _, j = stack.pop()
                result[j] = i - j
            stack.append((n, i))

        return result