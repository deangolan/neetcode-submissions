class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        subst = ""

        counts = {}
        for c in t:
            counts[c] = counts.get(c, 0) + 1

        l = 0
        r = len(t) - 1
        win = {}
        for c in s[l:r+1]:
            win[c] = win.get(c, 0) + 1
        
        # Keep exploring while not all chars are found.
        # If all chars are found try to move both left and right pointers.
        # Once right pointer is at the end, keep moving left pointer until
        # window is smaller than substring.
        while r - l >= len(t) - 1:
            if all(win.get(c, 0) >= counts[c] for c in t):
                if r - l + 1 < len(subst) or subst == "":
                    subst = s[l:r+1]
                win[s[l]] -= 1
                l += 1
            elif r < len(s) - 1:
                r += 1
                win[s[r]] = win.get(s[r], 0) + 1
            else:
                break

        return subst