class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                c = board[row][col]
                if c == ".":
                    continue
                else:
                    square = (row // 3) * 3 + col // 3
                    if c in rows[row] or c in cols[col] or c in squares[square]:
                        return False
                    # Otherwise, add to seen
                    rows[row].add(c)
                    cols[col].add(c)
                    squares[square].add(c)
        return True