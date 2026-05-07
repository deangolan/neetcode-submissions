import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        for sec in range(k):
            pile = heapq.heappop(gifts)
            heapq.heappush(gifts, -math.floor(math.sqrt(-pile)))

        return -sum(gifts)

