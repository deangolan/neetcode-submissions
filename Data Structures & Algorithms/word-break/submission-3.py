class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = { len(s): True }
        def dp(i):
            if i in memo:
                return memo[i]
            res = any(dp(i + len(word)) for word in wordDict if s[i:].startswith(word))
            memo[i] = res
            return res

        return dp(0)