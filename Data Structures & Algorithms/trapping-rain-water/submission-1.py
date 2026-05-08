class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])

        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(height[i], right[i+1])

        area = 0
        for i, h in enumerate(height):
            area += min(left[i], right[i]) - h

        return area