class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        return list(map(lambda x: x[0], sorted(freqs.items(), key=lambda x: -x[1])[0:k]))
