import random


class Cell:
    def __init__(self, mine=False, around_mines=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:

    def __init__(self, N, M):
        self.pole = [[0] * N for i in range(N)]
        self.init(N, M)

    def init(self, N, M):
        for i in range(N):
            for j in range(N):
                self.pole[i][j] = Cell()
        i = 0
        while i < M:
            x, y = random.randint(0, N - 1), random.randint(0, N - 1)
            if self.pole[x][y].mine is False:
                self.pole[x][y].mine = True
                self.update_around(x, y)
                i += 1

    def update_around(self, x, y):
        dim = len(self.pole[0][:])
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i < 0 or j < 0 or i >= dim or j >= dim:
                    continue
                self.pole[i][j].around_mines += 1
        self.pole[x][y].around_mines -= 1

    def show(self):
        dim = len(self.pole[0][:])
        temp = [['0'] * dim for i in range(dim)]
        for i in range(dim):
            for j in range(dim):
                if self.pole[i][j].fl_open is True:
                    temp[i][j] = str(self.pole[i][j].around_mines)
                    if self.pole[i][j].mine is True:
                        temp [i][j] = '*'
                else:
                    temp[i][j] = '#'
        for i in range(dim):
            print(' '.join([f'{x} ' for x in temp[i]]))
        pass


pole_game = GamePole(10, 12)
pole_game.show()
