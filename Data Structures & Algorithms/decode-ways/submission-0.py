class Solution:
    def numDecodings(self, s: str) -> int:
        # "0" -> 0
        # "2" -> 2
        # "12" -> (1, 2), (2)
        # "112" -> (11, 2), (1, 12), (1, 1, 2)
        # "1112" -> (11,12), (11,1,1,2), (1,11,2), (1,1,1,12), (1,1,1,2)
        memo = { len(s): 1 }

        def dp(i):
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0
            res = dp(i+1)
            if i < len(s) - 1 and int(s[i] + s[i+1]) <= 26:
                res += dp(i + 2)
            memo[i] = res
            return res
        
        return dp(0)