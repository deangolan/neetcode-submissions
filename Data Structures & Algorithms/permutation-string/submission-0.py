class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}
        for ch in s1:
            perm[ch] = perm.get(ch, 0) + 1
        
        seen = {}
        l = 0
        for r, ch in enumerate(s2):
            seen[ch] = seen.get(ch, 0) + 1

            while seen[ch] > perm.get(ch, 0) and l <= r:
                seen[s2[l]] = seen.get(s2[l], 0) - 1
                l += 1

            if all(n == seen.get(ch, 0) for ch, n in perm.items()):
                return True

        return False

