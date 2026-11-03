class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = set()

        def dfs(i, j, c):
            if i < 0 or j < 0 or i >= n or j >= m:
                return False
            if (i, j) not in visited:
                if board[i][j] == word[c]:
                    if c == len(word)-1:
                        return True
                    visited.add((i, j))
                    return dfs(i+1, j, c+1) or dfs(i, j+1, c+1) or dfs(i-1, j, c+1) or dfs(i, j-1, c+1)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                    visited = set()
        return False


