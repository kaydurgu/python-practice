import random

class Cell:
    def __init__(self, around_mines, mine) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    __isinstance = None
    
    def __init__(self, N, M) -> None:

        self.N = N
        self.M = M
        self.pole = []

    def init(self):  
        self.pole = [[Cell(0, False) for i in range(self.N)] for i in range(self.N)]  
        empty_fields = []
        # optimize : instead of using 2 dimensional array use total_amount_of_cells =  self.N * self.N
        # ex. choosen 14 out of 81 i , j = math.divmod(14 // self.N + 1 , 14 % self.N + 1)  i = 1, j = 5
        for i in range(self.N):
            for j in range(self.N):
                empty_fields.append([i, j])
                
        while self.M > 0 and empty_fields:
            choosen = random.choice(empty_fields)
            empty_fields.remove(choosen)
            print (choosen)
            self.pole[choosen[0]][choosen[1]].mine = True
            self.around(choosen[0], choosen[1])
            self.M-=1
        self.correct()

    def correct(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].mine:
                    self.pole[i][j].around_mines = 0     

    def around(self,x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x, new_y = i + x, j + y
                if new_x == x and new_y == y:
                    continue
                if new_x >= 0 and new_x < self.N and new_y >=0 and new_y < self.N:
                    self.pole[new_x][new_y].around_mines = self.pole[new_x][new_y].around_mines + 1
                    
    def show(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].mine:
                    print ('#', end = ' ')
                    continue
                print (self.pole[i][j].around_mines, end = ' ')
            print ()

pole_game = GamePole(10,20)
pole_game.init()
pole_game.show()
