class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        for n in nums:
            seen[n - 1] = n

        values = set(seen.values())  # O(n) to build once

        longest = 0
        for key in seen:
            if key not in values:  # only start chains from true beginnings
                chain_len = 0
                value = seen.get(key)
                while value is not None:
                    value = seen.get(value)
                    chain_len += 1
                longest = max(longest, chain_len)

        return longest
