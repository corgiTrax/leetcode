class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
      #total of 9+9+9 lists
        row_list = [[] for i in range(9)]
        col_list = [[] for i in range(9)]
        grid_list = [[] for i in range(9)]
        #build lists
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row_list[i].append(num)
                    col_list[j].append(num)    
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        num = board[i*3 + k][j*3 + l]
                        if num != '.':
                            grid_list[i*3 + j].append(num)

#        print(row_list)
#        print(col_list)
#        print(grid_list)

        for i in range(9):
            if not(self.check(row_list[i]) and self.check(col_list[i]) and self.check(grid_list[i])):
                return False

        return True

    def check(self, digit_list):
        #there are no repeat digit means valid
        return len(digit_list) == len(set(digit_list)) 


sol = Solution()
board = [[i for i in range(9)] for i in range(9)]
#print(board)
sol.isValidSudoku(board)
