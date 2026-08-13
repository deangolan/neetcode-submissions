class Solution:
    def numSquares(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[1] = 1
        for i in range(1, n + 1):
            res = i
            for j in range(1, i):
                square = j ** 2
                if square > i:
                    break
                res = min(res, 1 + memo[i - square])
            memo[i] = res

        return memo[n]

