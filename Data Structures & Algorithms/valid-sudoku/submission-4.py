class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        squareHash = {}
        for i in range(n):
            rowHash = {}
            colHash = {}
            for j in range(m):
                row = board[i][j]
                col = board[j][i]
                square = (i//3, j//3)
                # if row == "." or col == ".":
                #     continue
                if row != ".":
                    if row not in rowHash:
                        rowHash[row] = 0
                    rowHash[row] += 1
                    if rowHash[row] > 1:
                        return False
                if col != ".":
                    if col not in colHash:
                        colHash[col] = 0
                    colHash[col] += 1
                    if colHash[col] > 1:
                        return False

                if row != ".":
                    if square not in squareHash:
                        squareHash[square] = {}
                    if row in squareHash[square]:
                        return False
                    squareHash[square][row] = 1
                

        return True


        