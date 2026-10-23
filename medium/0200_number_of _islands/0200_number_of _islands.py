from collections import deque

class Solution:
    def find_first_unvisited_land(
            self, grid: list[list[str]],
            visited: list[list[bool]], m: int, n: int
    ) -> tuple[int, int]:
        for i in range(m):
            for j in range(n):
                if (not visited[i][j]) and grid[i][j] == "1":
                    return i, j
        return -1, -1

    def possible_land_neighbors(self, grid: list[list[str]], m: int, n: int, i: int, j: int):
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        land_neighbors = []
        for dir in dirs:
            dir_x, dir_y = dir[0], dir[1]
            new_x = i + dir_x
            new_y = j + dir_y
            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1":
                land_neighbors.append((new_x, new_y))

        return land_neighbors


    def bfs(self, grid: list[list[str]], visited: list[list[bool]],
            m: int, n: int, i: int, j: int):
        queue = deque([(i, j)])
        while queue:
            first = queue.popleft()
            visited[first[0]][first[1]] = True
            land_neighbors = self.possible_land_neighbors(grid, m, n, first[0], first[1])
            for x, y in land_neighbors:
                if not visited[x][y]:
                    queue.append((x, y))
                    visited[x][y] = True

    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for __ in range(n)] for _ in range(m)]
        islands = 0
        while True:
            first_unvisited_land = self.find_first_unvisited_land(grid, visited, m, n)
            if first_unvisited_land == (-1, -1):
                break
            i, j = first_unvisited_land
            self.bfs(grid, visited, m, n, i, j)
            islands += 1

        return islands

