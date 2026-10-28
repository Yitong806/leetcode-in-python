class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        return self.mle(grid)

    def mle(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for i in range(1, m):
            up_xors = dp[i - 1][0]
            for xor in up_xors:
                dp[i][0].add(xor ^ grid[i][0])

        for j in range(1, n):
            left_xors = dp[0][j - 1]
            for xor in left_xors:
                dp[0][j].add(xor ^ grid[0][j])

        for i in range(1, m):
            for j in range(1, n):
                up_xors = dp[i - 1][j]
                left_xors = dp[i][j - 1]
                for xor in up_xors:
                    dp[i][j].add(xor ^ grid[i][j])
                for xor in left_xors:
                    dp[i][j].add(xor ^ grid[i][j])

        return min(dp[m - 1][n - 1])


