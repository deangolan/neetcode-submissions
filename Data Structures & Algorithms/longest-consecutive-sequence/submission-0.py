class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        for n in nums:
            seen[n-1] = n
            
        longest = 0
        for key, value in seen.items():
            chain_len = 0
            while value is not None: 
                value = seen.get(value, None)
                chain_len += 1

            longest = max(longest, chain_len)
            
        return longest