class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        self.dfs(board, row, col)
        return board

    def dfs(self, board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'E':
            return
        mines = self.get_mines(board, row, col)
        if mines > 0:
            board[row][col] = str(mines)
        else:
            board[row][col] = 'B'
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    self.dfs(board, row + i, col + j)

    def get_mines(self, board, row, col):
        mines = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                r, c = row + i, col + j
                if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                    continue
                if board[r][c] == 'M' or board[r][c] == 'X':
                    mines += 1
        return mines