class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#' for  _ in range(n)] for _ in range(m)]
        for i in range(m):
            grid[i][0] = '.'
        for j in range(n):
            grid[m - 1][j] = '.'
        return [''.join(l) for l in grid]