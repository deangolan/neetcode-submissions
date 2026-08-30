class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = {}
        def dp(numRows):
            if numRows == 1:
                return [[1]]
            if numRows in memo:
                return memo[numRows]

            rows = dp(numRows-1)
            row = [0] * numRows
            for i in range(numRows):
                row[i] = (rows[-1][i-1] if i-1 >= 0 else 0) + (rows[-1][i] if i < numRows - 1 else 0)
            rows.append(row)
            memo[numRows] = rows
            return rows

        return dp(numRows)