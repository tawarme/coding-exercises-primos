class Solution:
    def rotate_pixel_set(self, curr, matrix):
        h = len(matrix[0]) - 1
        w = len(matrix) - 1

        rx, ry = curr
        pixel_set = [[rx, ry], 
                     [ry, w - rx], 
                     [w - rx, h - ry], 
                     [h - ry, rx]]

        last = matrix[pixel_set[3][0]][pixel_set[3][1]]

        prev = last

        for pixel in pixel_set:
            pmem = matrix[pixel[0]][pixel[1]]
            matrix[pixel[0]][pixel[1]] = prev

            prev = pmem
            

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        curr_start = 0
        curr_end = len(matrix) - 1 # -1 because we dont want to touch the last pixel

        row = 0
        while curr_start < len(matrix) // 2 :
            for curr in range(curr_start, curr_end):
                self.rotate_pixel_set((curr, row), matrix)

            curr_start += 1
            curr_end -= 1
            row += 1
