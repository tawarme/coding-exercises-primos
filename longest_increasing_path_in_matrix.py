class Solution:
    def go(self, matrix, row, col, mem):
        if mem[row][col]:
            return mem[row][col]

        DIR = [[0,1], [0,-1], [1,0], [-1,0]]

        local_max_len = 0
        for dir in DIR:
            neirow = row + dir[0]
            neicol = col + dir[1]

            if not (0 <= neirow < len(matrix) and 0 <= neicol < len(matrix[0])):
                continue

            if matrix[neirow][neicol] > matrix[row][col]:
                local_max_len = max(local_max_len, self.go(matrix, neirow, neicol, mem))

        mem[row][col] = local_max_len + 1

        return mem[row][col]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        mem = [[0 for col in range(cols)] for row in range(rows)]

        max_len = 0
        for row in range(rows):
            for col in range(cols):
                max_len = max(max_len, self.go(matrix, row, col, mem))

        return max_len
