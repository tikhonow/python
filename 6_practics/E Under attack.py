WHITE = 1
BLACK = 2

def print_board(board):  # Распечатать доску в текстовом виде
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row + 1, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        alphabet = 'ABCDEFGH'
        print(alphabet[col], end='    ')
    print()

def correct_coords(row, col):
    '''Функция проверяет, что координаты (row, col) лежат
    внутри доски'''
    return 0 <= row < 8 and 0 <= col < 8

def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE

def parse_coords(coords):
    '''Считывания кординат'''
    try:
        cords1,cords2 = coords.split()
        col, row, col1, row1 = cords1[0],cords1[1],cords2[0],cords2[1]
        col, col1 = col.lower(), col1.lower()
    except ValueError:
        print('Вы ввели координаты неправильно! Проверьте роаскладку и попробуйте еще раз!')
        return main()
    row, row1 = int(row) - 1, int(row1) - 1
    alphabet = 'abcdefgh'
    for i in range(8):
        if alphabet[i] == col:
            col = i
        if alphabet[i] == col1:
            col1 = i
    return row, col, row1, col1

class Board:
    '''Класс доски  '''
    def __init__(self):
        self.color = WHITE
        self.field = [[None] * 8 for row in range(8)]
        #Задаем начальное расположение фигур на доске:
        #Верх
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        #Внизе
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела.'''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]

    def move_piece(self, row, col, row1, col1):
        ''' Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False '''

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False

        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        else:
            # TODO Если мы перемещаемся на фигуру
            pass

        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color) # поменять цвет
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if type(self.get_piece(row, col)) is not Pawn:
            return False
        new_pawn = None
        color = self.get_piece(row, col).get_color()
        if char == 'Q':
            new_pawn = Queen(color)
        elif char == 'R':
            new_pawn = Rook(color)
        elif char == 'B':
            new_pawn = Bishop(color)
        elif char == 'N':
            new_pawn = Knight(color)
        if self.move_piece(row, col, row1, col1):
            self.field[row1][col1] = new_pawn
            return True
        return False

 
    def is_under_attack(self, row, col, color):
        '''Возращает True, если поле с координатами (row, col)находится под боем хотя бы одной фигуры цвета color.'''
        for i in range(len(self.field)):
            for j, piece in enumerate(self.field[i]):
                if piece is not None and piece.get_color() == color and          piece.can_move(self, i, j, row, col):
                    return True
        else:
             return False
    
    def is_piece_moved(self, piece):
        if piece.is_moved > 0:
            return True
        return False

class Piece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Rook(Piece):
    '''Класс ладьи'''
    def __init__(self, color):
        super().__init__(color)
        self.not_moved = True

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        self.moved()
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def moved(self):
        self.not_moved = False

class Pawn(Piece):
    '''Класс пешки'''
    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1 and board.field[row1][col1] is None:
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1 and (col + 1 == col1 or col - 1 == col1))

class Knight(Piece):
    '''Класс коня'''
    def char(self):
        return 'N'  # kNight, буква 'K' уже занята королём

    def can_move(self, board, row, col, row1, col1):
        x, y = row, col
        coords = [
            (x - 2, y + 1), (x - 2, y - 1),
            (x - 1, y - 2), (x + 1, y - 2),
            (x + 2, y - 1), (x + 2, y + 1),
            (x + 1, y + 2), (x - 1, y + 2)
        ]

        if (row1, col1) in coords and row1 in range(8) and col1 in range(8):
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

class King(Piece):
    '''Класс короля'''
    def __init__(self, color):
        self.is_moved = 0

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        stepr = row1 - row
        stepc = col1 - col
        if not (board.get_piece(row1, col1) is None) and board.cell(row1, col1)[0] == board.cell(row, col)[0]:
            return False

        if ((stepr == 1 or stepr == -1 or stepr == 0) and (stepc == 1 or stepc == -1 or stepc == 0)) and (0 <= row <= 7) and (0 <= col <= 7):
            if row == row1 and col == col1:
                return False
            if board.is_under_attack(row1, col1):
                return False
            return True
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

class Bishop(Piece):
    '''Класс слона'''
    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        my_row, my_col = row, col
        step_row = -1 if (row > row1) else 1
        step_col = -1 if (col > col1) else 1
        if abs(row - row1) != abs(col - col1):
            return False
        for i in range(abs(row - row1) - 1):
            my_row, my_col = my_row + step_row, my_col + step_col
            if board.get_piece(my_row, my_col) is not None:
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

class Queen(Piece):
    '''Класс ферзя'''
    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        my_row, my_col = row, col
        if board.get_piece(row1, col1) and board.get_piece(row1, col1).get_color() == self.color:
            return False
        if row == row1 or col == col1:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                if not (board.get_piece(r, col) is None):
                    return False
            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                if not (board.get_piece(row, c) is None):
                    return False
            return True
        if abs(row - row1) != abs(col - col1):
            return False
        step_row = -1 if (row > row1) else 1
        step_col = -1 if (col > col1) else 1
        for i in range(abs(row - row1) - 1):
            my_row, my_col = my_row + step_row, my_col + step_col
            if not (board.get_piece(my_row, my_col) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

def main():
    print("Пример 1",'\n')
    board = Board()
    
    board.field = [([None] * 8) for i in range(8)]
    board.field[0][0] = Rook(WHITE)
    board.field[1][2] = Bishop(WHITE)
    coords = ((0, 0), (1, 2))

    for row in range(7, -1, -1):
        for col in range(8):
            if (row, col) in coords:
                print('W',end=' ')
            elif board.is_under_attack(row, col, WHITE):
                print('x', end=' ')
            else:
                print('-', end=' ')
        print()

    print("Пример 2",'\n')
    board = Board()
    
    board.field = [([None] * 8) for i in range(8)]
    board.field[0][5] = Rook(WHITE)
    board.field[1][2] = Bishop(WHITE)
    board.field[7][6] = Knight(WHITE)
    coords = ((0, 5), (1, 2), (7, 6))

    for row in range(7, -1, -1):
        for col in range(8):
            if (row, col) in coords:
                print('W',end=' ')
            elif board.is_under_attack(row, col, WHITE):
                print('x', end=' ')
            else:
                print('-', end=' ')
        print()

    print("Пример 3",'\n')
    board = Board()

    board.field = [([None] * 8) for i in range(8)]
    board.field[0][5] = Rook(WHITE)
    board.field[1][2] = Bishop(WHITE)
    board.field[7][6] = Knight(BLACK)
    w_coords = ((0, 5), (1, 2))
    b_coords = ((7, 6), )

    print('White:')
    for row in range(7, -1, -1):
        for col in range(8):
            if (row, col) in w_coords:
                print('W',end=' ')
            elif board.is_under_attack(row, col, WHITE):
                print('x',end=' ')
            else:
                print('-',end=' ')
        print()
    print()

    print('Black:')
    for row in range(7, -1, -1):
        for col in range(8):
            if (row, col) in b_coords:
                print('B',end=' ')
            elif board.is_under_attack(row, col, BLACK):
                print('x',end=' ')
            else:
                print('-',end=' ')
        print()
    print()

#Запуск программы
if __name__ == "__main__":
    main()