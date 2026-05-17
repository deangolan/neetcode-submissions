class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, c in enumerate(s):
            if not c in seen:
                seen[c] = i
            else:
                seen[c] = float('inf')

        res = min(seen.values())
        return res if res != float('inf') else -1