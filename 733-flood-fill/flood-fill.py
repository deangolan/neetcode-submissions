class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW = len(image)
        COL = len(image[0])

        starting_color = image[sr][sc]

        def dfs(i, j): 
            if i < 0 or i >= ROW or j < 0 or j >= COL or image[i][j] != starting_color:
                return
            image[i][j] = color
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        if starting_color != color:
            dfs(sr, sc)
        return image