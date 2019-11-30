class Cell:
    def __init__(self, clicked=False, val='-'):
        self.clicked = clicked
        self.val = val

    def click(self, val):
        self.val = val


class Board:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.arr = []
        self.step = 0

        for i in range(n):
            self.arr.append([])
            for j in range(m):
                self.arr[-1].append(Cell())

    def get_val(self):
        return ['X', 'O'][self.step % 2]

    def click(self, x, y):
        if self.arr[x][y].val == '-':
            self.arr[x][y].click(self.get_val())
            self.step += 1
