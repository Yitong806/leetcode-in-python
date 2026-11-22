class Solution:
    def __init__(self):
        self.ans = []

    def solveNQueens(self, n: int) -> list[list[str]]:
        self.ans.clear()
        cb = [[0 for _ in range(n)] for _ in range(n)]
        self.dfs(cb, 0, n)
        return self.ans

    def current_available(self, x, y, chessboard: list[list[int]], n: int):
        av = [[True for _ in range(n)] for _ in range(n)]
        dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        for i in range(n):
            for j in range(n):
                if chessboard[i][j] != 1:
                    continue
                av[i][j] = False
                for direction in dirs:
                    step = 1
                    while True:
                        new_i = i + direction[0]*step
                        new_j = j + direction[1]*step
                        if not self.check_boundary(new_i, new_j, n):
                            break
                        av[new_i][new_j] = False
                        step += 1
        return av[x][y]


    def check_boundary(self, i, j, n):
        return 0 <= i < n and 0 <= j < n

    def chessboard2str(self, chessboard: list[list[int]], n: int) -> list[str]:
        ans = []
        for i in range(n):
            row = []
            for j in range(n):
                if chessboard[i][j] == 1:
                    row.append('Q')
                else:
                    row.append('.')
            ans.append(''.join(row))
        return ans

    def dfs(self, chessboard: list[list[int]], current_row: int, n: int):
        if current_row == n:
            self.ans.append(self.chessboard2str(chessboard, n))
            return

        for i in range(n):
            if not self.current_available(current_row, i, chessboard, n):
                continue
            chessboard[current_row][i] = 1
            self.dfs(chessboard, current_row + 1, n)
            chessboard[current_row][i] = 0
