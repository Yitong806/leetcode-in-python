class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not word:
            return True
        if not len(board) or not len(board[0]):
            return False
        possible_start_positions: list[tuple[int, int]] = self.possible_start(board, word)
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        any_success = False
        for i, j in possible_start_positions:
            visited[i][j] = True
            any_success = any_success or self.search(board, word, i, j, visited, 1)
            visited[i][j] = False

        return any_success

    def possible_start(self, board: list[list[str]], word: str) -> list[tuple[int, int]]:
        first_char = word[0]
        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == first_char:
                    ans.append((i, j))
        return ans

    def search(self, board: list[list[str]], word: str, i: int, j: int, visited: list[list[bool]], index: int) -> bool:
        if index == len(word):
            return True
        any_success = False
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for d in dirs:
            new_i, new_j = i + d[0], j + d[1]
            if not self.checkboundary(new_i, new_j, board):
                continue
            if board[new_i][new_j] != word[index]:
                continue
            if visited[new_i][new_j]:
                continue
            visited[new_i][new_j] = True
            any_success = any_success or self.search(board, word, new_i, new_j, visited, index + 1)
            visited[new_i][new_j] = False

        return any_success

    def checkboundary(self, i: int, j: int, board: list[list[str]]) -> bool:
        return 0 <= i < len(board) and 0 <= j < len(board[0])