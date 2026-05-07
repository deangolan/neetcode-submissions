class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        seen = {}
        l = 0
        for r, char in enumerate(s):
            seen[char] = seen.get(char, 0) + 1
            
            while seen[char] > 1 and l < r:
                seen[s[l]] -= 1
                l += 1
                
            max_len = max(max_len, r - l + 1)

        return max_len