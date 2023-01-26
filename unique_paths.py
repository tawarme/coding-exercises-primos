        grid = []
        for i in range(m+1):
            grid.append([0 for j in range(n+1)])

        grid[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == j == 1:
                    continue

                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[-1][-1]
