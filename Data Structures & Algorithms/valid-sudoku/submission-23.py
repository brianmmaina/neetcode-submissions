class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                value = board[r][c]
                square_key = (r//3, c//3)

                if(value in rows[r] or value in cols[c] or value in squares[square_key]):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[square_key].add(value)
        
        return True
                   
        