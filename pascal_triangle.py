class Solution:
    def generate(self, numRows: int):
        rows = [[1]]
        prev_row = [1]

        for row_i in range(1, numRows):
            row = []
            for item_i in range(row_i+1):
                row.append((prev_row[item_i-1] if item_i-1 >= 0 else 0) + (prev_row[item_i] if item_i <= row_i-1 else 0))
            prev_row = row
            rows.append(row)

        return rows
