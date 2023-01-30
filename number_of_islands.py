class Solution:
    def dfs(self, row, col, grid):

        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == "0":
            return
        #if grid[row][col] == "0":
        #    #return 0
        #    return

        grid[row][col] = "0"

        DIRECTIONS = [[0,1], [1,0], [-1, 0], [0,- 1]]

        for dir in DIRECTIONS:
            neirow = row + dir[0]
            neicol = col + dir[1]

            #if not (0 <= neirow < len(grid) and 0 <= neicol < len(grid[0])):
            #    continue

            self.dfs(neirow, neicol, grid)

        #return 1


    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        island_counter = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_counter += 1
                    self.dfs(row, col, grid)

        return island_counter