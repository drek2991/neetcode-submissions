class Solution:
    def inBounds(self, n: int, m: int, r: int, c: int) -> bool:
        return 0 <= r and r < n and 0 <= c and c < m
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        stk = []
        ans = 0
        diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    stk.append((i, j))
                    visited.add((i, j))
                    while len(stk) > 0:
                        curr = stk.pop()
                        for dx, dy in diff:
                            row = curr[0]+dx
                            col = curr[1]+dy
                            if self.inBounds(n, m, row, col) and (row, col) not in visited and grid[row][col] == "1":
                                stk.append((row, col))
                                visited.add((row, col))
                    ans += 1

        return ans

                