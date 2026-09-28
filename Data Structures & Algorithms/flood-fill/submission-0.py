class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        value = image[sr][sc]
        visited = set()
        def dfs(i, j):
            if (i, j) in visited:
                return
            if 0 <= i and i < m and 0 <= j and j < n and image[i][j] == value:
                image[i][j] = color
                visited.add((i, j))
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
        dfs(sr, sc)
        return image
            


