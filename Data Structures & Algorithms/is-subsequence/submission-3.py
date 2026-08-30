class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        si = 0
        for ch in t:
            if ch == s[si]:
                si += 1
                if si == len(s):
                    return True
        return False