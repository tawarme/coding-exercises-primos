class Solution:
    def val(self, val_map, i, j, board):
        val = board[i][j]

        if val == ".":
            return True

        if val_map.get(val):
            return False

        val_map[val] = True

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            val_row = {}
            for j in range(9):
                if not self.val(val_row, i, j, board):
                    return False

        for j in range(9):
            val_col = {}
            for i in range(9):
                if not self.val(val_col, i, j, board):
                    return False

        for sqr in range(9):
            sqr_i = sqr // 3 * 3
            sqr_j = sqr % 3 * 3

            val_cube = {}
            for i in range(sqr_i, sqr_i + 3):
                for j in range(sqr_j, sqr_j + 3):
                    if not self.val(val_cube, i, j, board):
                        return False

        return True
                    
