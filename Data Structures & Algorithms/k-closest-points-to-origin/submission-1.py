import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-p[0]**2 - p[1]**2, i) for i, p in enumerate(points)]
        heapq.heapify(heap)
        for _ in range(len(points) - k):
            heapq.heappop(heap)
        return [points[i] for _, i in heap]