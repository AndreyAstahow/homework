import random

print('-' * 23)
print('Добро пожаловать в игру')
print('-' * 5, 'Морской бой', '-' * 5)
print('-' * 23,)

board = [['.'] * 6 for i in range(6)]

class Board:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def user_board(self):
        print('  0 1 2 3 4 5')
        for i in range(6):
            print(f'{i}', *board[i])
        return

    def enemy_board(self):
        print('  0 1 2 3 4 5')
        for i in range(6):
            print(f'{i}', *board[i])

    user_board(board)
    enemy_board(board)

    def add_ship(self):
        pass

    def contour():
        pass
    
    def out():
        pass
    
    def shot(self):
        pass
        


class BoardOutExceptoin:
    pass


class Player:

    def __init__(self, User, Al):
        self.User = User
        self.Al = Al

class Al(Player):
    pass


class User(Player):
    pass

class Dot:

    def __init__(self, y, x):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Dot):
            raise TypeError(f'{other} не является точкой')
        return self.x == other.x and self.y == other.y

class Ship:

    def __init__(self, long, point, direction):
        self.long = long
        self.point = point
        self.direction = direction
    
    def return_dot(self):
        list_dot = []
        y = self.point.y
        x = self.point.x
        i = 0
        for i in range(self.long):
            if self.direction == 'Г':
                point_ship = y, x
                list_dot.append(point_ship)
                x += 1
            else:
                point_ship = y, x
                list_dot.append(point_ship)
                y += 1
        return list_dot


ship_1 = Ship(2, Dot(4, 3), 'В')
