class Solution:
       def isValidSudoku(self, board: List[List[str]]) -> bool:
           for row in board:
               rowFreq = {}

               for num in row:
                   if num != ".":
                       rowFreq[num] = rowFreq.get(num, 0) + 1

               for freq in rowFreq.values():
                   if freq > 1:
                       return False

           for num in range(len(board[1])):
               colFreq = {}
               col = [row[num] for row in board]

               for num2 in col:
                   if num2 != ".":
                       colFreq[num2] = colFreq.get(num2, 0) + 1

               for freq in colFreq.values():
                   if freq > 1:
                       return False

           for boxRow in range(0, 9, 3):
               for boxCol in range(0, 9, 3):
                   squareFreq = {}

                   for r in range(boxRow, boxRow + 3):
                       for c in range(boxCol, boxCol + 3):
                           if board[r][c] != ".":
                               squareFreq[board[r][c]] = squareFreq.get(board[r][c], 0) + 1

                   for freq in squareFreq.values():
                       if freq > 1:
                           return False

           return True