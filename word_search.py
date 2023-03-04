class Solution:
    def go(self, row, col, board, i, word):
        DIR = [[0,1], [0,-1], [1, 0], [-1, 0]]

        if i == len(word) -1 :
            return True

        ch = board[row][col]

        board[row][col] = "#"

        for dir in DIR:
            newrow = row + dir[0]
            newcol = col + dir[1]

            if not (0 <= newrow < len(board) and 0 <= newcol < len(board[0])):
                continue

            if board[newrow][newcol] == word[i + 1]:
                if self.go(newrow, newcol, board, i + 1, word):
                    return True
        
        board[row][col] = ch
            

        

    def exist(self, board: List[List[str]], word: str) -> bool:

        if len(word) > len(board) * len(board[0]):
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.go(row, col, board, 0, word):
                        return True
