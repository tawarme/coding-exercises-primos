class Solution:
    def dfs(self, row, col, reachable, heights):
        DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        reachable[row][col] = True

        for dira in DIRECTIONS:
            neirow = row + dira[0]
            neicol = col + dira[1]

            if not (0 <= neirow < len(heights) and 0 <= neicol < len(heights[0])):
                continue

            if reachable[neirow][neicol]:
                continue

            if heights[neirow][neicol] < heights[row][col]:
                continue
            
            self.dfs(neirow, neicol, reachable, heights)

    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0 or len(heights[0]) == 0:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacific = [[None for col in range(cols)] for row in range(rows)]
        atlantic = [[None for col in range(cols)] for row in range(rows)]

        for i in range(rows):
            self.dfs(i, 0, pacific, heights)
            self.dfs(i, cols - 1, atlantic, heights)

        for i in range(cols):
            self.dfs(0, i, pacific, heights)
            self.dfs(rows - 1, i, atlantic, heights)

        ans = []

        for row in range(rows):
            for col in range(cols):
                if atlantic[row][col] and pacific[row][col]:
                    ans.append([row, col])

        return ans
