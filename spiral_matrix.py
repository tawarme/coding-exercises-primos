class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        DIR = [[0,1], [1,0], [0,-1], [-1,0]]

        #cur = [0, 0]
        cur = [-1, -1]
        #cur_dir = DIR[0]
        cur_dir = DIR[3]

        dat = []
        
        turns = -1

        rows = len(matrix)
        cols = len(matrix[0])

        while True:
            if not(0 <= cur[0] < rows and 0 <= cur[1] < cols) or matrix[cur[0]][cur[1]] is None:
                #print("TURN")
                cur[0] -= cur_dir[0]
                cur[1] -= cur_dir[1]
                #print("cur turn", cur)

                turns += 1
                cur_dir = DIR[turns % 4]
            
            
                cur[0] += cur_dir[0]
                cur[1] += cur_dir[1]
            
            #print(cur)

            if not(0 <= cur[0] < rows and 0 <= cur[1] < cols):
                return dat

            val = matrix[cur[0]][cur[1]]

            if val is None:
                return dat
            
            dat.append(val)

            matrix[cur[0]][cur[1]] = None

            cur[0] += cur_dir[0]
            cur[1] += cur_dir[1]

