class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1

        minHeap = []
        for n, freq in freqs.items():
            heapq.heappush(minHeap, (freq, n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [n for _, n in minHeap]