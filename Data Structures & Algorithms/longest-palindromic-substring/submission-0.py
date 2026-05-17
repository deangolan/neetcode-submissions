class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force
        longest = ""
        res_len = 0

        for i, c in enumerate(s):
            # odd palindrome
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if res_len < r - (l + 1):
                longest = s[l+1:r]
                res_len = r - (l + 1)

            # even palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if res_len < r - (l + 1):
                longest = s[l+1:r]
                res_len = r - (l + 1)
        return longest