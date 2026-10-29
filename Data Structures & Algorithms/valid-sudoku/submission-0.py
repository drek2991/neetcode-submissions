class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row -> set
        # col -> set
        # box -> set
        rows = {}
        cols = {}
        box = {}
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    val = int(board[i][j])

                    if i not in rows:
                        rows[i] = set()
                        rows[i].add(val)
                    elif val in rows[i]:
                        return False
                    else:
                        rows[i].add(val)

                    if j not in cols:
                        cols[j] = set()
                        cols[j].add(val)
                    elif val in cols[j]:
                        return False
                    else:
                        cols[j].add(val)

                    b = 3 * (i//3) + j//3
                    if b not in box:
                        box[b] = set()
                        box[b].add(val)
                    elif val in box[b]:
                        return False
                    else:
                        box[b].add(val)
        return True

                
    


