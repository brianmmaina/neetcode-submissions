class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # cols[c] stores numbers already seen in column c
        cols = defaultdict(set)

        # rows[r] stores numbers already seen in row r
        rows = defaultdict(set)

        # squares[(r // 3, c // 3)] stores numbers already seen
        # in each 3x3 box
        squares = defaultdict(set)

        # Traverse every cell in the 9x9 board
        for r in range(9):
            for c in range(9):

                # Ignore empty cells
                if board[r][c] == ".":
                    continue

                value = board[r][c]

                # Find which 3x3 square this cell belongs to
                square_key = (r // 3, c // 3)

                # If the value already exists in the current row,
                # current column, or current 3x3 square, board is invalid
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in squares[square_key]
                ):
                    return False

                # Mark this value as seen
                rows[r].add(value)
                cols[c].add(value)
                squares[square_key].add(value)

        # No duplicates found
        return True