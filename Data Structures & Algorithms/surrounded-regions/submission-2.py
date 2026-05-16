class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])

        def dfs(i, j):
            if i < 0 or i >= ROW or j < 0 or j >= COL or board[i][j] != 'O':
                return
            board[i][j] = 'S'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if i in (0, ROW-1) or j in (0, COL-1):
                    dfs(i, j)
        
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'