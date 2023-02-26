class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):

                live_count = 0
                #print("inspect", row, col)
                for neirow in range(row -1, row + 2):
                    for neicol in range(col -1, col + 2):
                        if not (0 <= neirow < rows and 0 <= neicol < cols):
                            continue

                        if neirow == row and neicol == col:
                            continue

                        if board[neirow][neicol] & 1:
                            #print("live nei found", neirow, neicol)
                            live_count += 1

                            if live_count > 3:
                                break

                if 2 <= live_count <= 3:
                    if not board[row][col] and live_count == 3:
                        board[row][col] |= 0b10
                else:
                    if board[row][col]:
                        board[row][col] |= 0b10


        for row in range(rows):
            #print(board[row])
            for col in range(cols):
                if board[row][col] & 0b10:
                    board[row][col] = (board[row][col] & 1) ^ 1
