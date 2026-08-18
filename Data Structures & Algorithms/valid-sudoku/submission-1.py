class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.check_row(row):
                return False

        for col in range(len(board[0])):
            if not self.check_col( board, col):
                return False

        for y in range(1, len(board), 3):
            for x in range(1, len(board[0]), 3):
                if not self.check_box(board, (x,y)):
                    return False
        
        return True


    def check_box(self, board: List[List[str]], point) -> bool:
        x, y = point
        dirs = [
         (x-1, y-1),
         (x, y-1),
         (x+1, y-1),
         (x, y),
         (x-1, y),
         (x+1, y),
         (x-1, y+1),
         (x, y+1),
         (x+1, y+1)
        ]

        counter = {}
        for i in range(len(dirs)):
            tx, ty = dirs[i]
            num = board[ty][tx]
            if num != '.' and counter.get(num):
                return False
            counter[num] = True

        return True

    def check_row(self, row: List[str]) -> bool:
        counter = {}
        for num in row:
            if num != '.' and counter.get(num):
                return False
            counter[num] = True
        return True

    def check_col(self, board: List[List[str]], i: int) -> bool:
        counter = {}
        for row in board:
            num = row[i]
            if num != '.' and counter.get(num):
                return False
            counter[num] = True
        return True