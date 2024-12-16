from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = defaultdict(set)
        col_sets = defaultdict(set)
        sq_sets = defaultdict(set)

        for row in range(9):
            for col in range(9):
                sq = (row // 3, col // 3)
                if board[row][col] == ".":
                    continue
                elif board[row][col] in row_sets[row] or board[row][col] in col_sets[col] or board[row][col] in sq_sets[sq]:
                    return False
                row_sets[row].add(board[row][col])
                col_sets[col].add(board[row][col])
                sq_sets[sq].add(board[row][col])

        return True  