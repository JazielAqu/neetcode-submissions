class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                sqr_idx = r//3 * 3 + c//3

                if value in row[r] or value in col[c] or value in squares[sqr_idx]:
                    return False

                row[r].add(value)
                col[c].add(value)
                squares[sqr_idx].add(value)

        return True

        
        

        