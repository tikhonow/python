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
        col, row, col1, row1 = coords.split()
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

    def is_piece_moved(self, piece):
        if piece.is_moved > 0:
            return True
        return False

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

    def is_under_attack(self, row1, col1, color):
        if self.field[row1][col1] is not None:
            if self.field[row1][col1].color == color:
                return True
        for row in range(8):
            for col in range(8):
                if self.get_piece(row, col) is not None:
                    if self.get_piece(row, col).get_color() == color:
                        if self.get_piece(row, col).can_move(self, row, col, row1, col1):
                            return True
        return False

    def ext_is_under_attack(self, row1, col1, color):
        if self.get_piece(row1, col1) is not None:
            if self.get_piece(row1, col1).color == color:
                return self.get_piece(row1, col1), row1, col1
        for row in range(8):
            for col in range(8):
                if self.get_piece(row, col) is not None:
                    if self.get_piece(row, col).get_color() == color:
                        if self.get_piece(row, col).can_move(self, row, col, row1, col1):
                            return self.get_piece(row, col), row, col
        return False

    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                if type(self.field[row][col]) == King and self.field[row][col].color == color:
                    return row, col

    def Can_king_move(self, color):
        rowk, colk = self.find_king(color)
        for row in range(-1, 2, 1):
            for col in range(-1, 2, 1):
                if correct_coords(rowk + row, colk + col):
                    if self.get_piece(rowk, colk).can_move(self, rowk, colk, rowk + row, colk + col) and \
                            not (self.is_under_attack(rowk + row, colk + col, opponent(self.color))):
                        return True
        return False

    def Piece_can_save_king(self, color):
        rowk, colk = self.find_king(color)
        piece, rowp, colp = self.ext_is_under_attack(rowk, colk, opponent(color))
        for row in range(-1, 2, 1):
            for col in range(-1, 2, 1):
                if correct_coords(rowk + row, colk + col):
                    if piece.can_attack(self, rowp, colp, rowk + row, colk + col):
                        if self.is_under_attack(rowk + row, colk + col, self.color):
                            dpiece, rowdp, coldp = self.ext_is_under_attack(rowk + row, colk + col, self.color)
                            if rowdp != row + rowk and coldp != col + colk:
                                self.field[rowdp][coldp] = None
                                self.field[rowk + row][colk + col] = dpiece
                                if not (piece.can_attack(self, rowp, colp, rowk + row, colk + col)):
                                    self.field[rowdp][coldp] = dpiece
                                    self.field[rowk + row][colk + col] = None
                                    return True
                                self.field[rowdp][coldp] = dpiece
                                self.field[rowk + row][colk + col] = None
        return False
    
    def castling0(self, row, col, row1, col1):
        num = 0 if self.color == WHITE else 7
        if row != num or col != 4:
            return False
        elif row1 != num or col1 != 2:
            return False
        elif self.is_piece_moved(self.get_piece(num, 4)) or self.is_piece_moved(self.get_piece(num, 0)):
            return False
        else:
            for c in range(1, 4):
                if self.get_piece(num, c) is not None or self.is_under_attack(num, c, opponent(self.color)):
                    return False
        piece = self.get_piece(num, 4)
        self.field[num][4] = None
        self.field[num][2] = piece
        piece = self.get_piece(num, 0)
        self.field[num][0] = None
        self.field[num][3] = piece
        return True

    def castling7(self, row, col, row1, col1):
        num = 0 if self.color == WHITE else 7
        if row != num or col != 4:
            return False
        elif row1 != num or col1 != 6:
            return False
        elif self.is_piece_moved(self.get_piece(num, 4)) or self.is_piece_moved(self.get_piece(num, 7)):
            return False
        else:
            for c in range(5, 7):
                if self.get_piece(num, c) is not None or self.is_under_attack(num, c, opponent(self.color)):
                    return False
        piece = self.get_piece(num, 4)
        self.field[num][4] = None
        self.field[num][6] = piece
        piece = self.get_piece(num, 0)
        self.field[num][7] = None
        self.field[num][5] = piece
        return True

class Piece:
    def __init__(self, color):
        self.color = color
        self.is_moved = 0

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
    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        return True  # Заглушка

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
    # Создаём доску
    board = Board()
    # Цикл ввода команд игроков
    while True:
        # Выводим доску
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    <coord1> <coord2>     -- ход из клетки (coord1) в клетку (coord2)')

        # Выводим чей ход
        if board.current_player_color() == WHITE:
            print('Ход белых: ', end='')
        else:
            print('Ход чёрных: ', end='')

        command = input()
        if command == 'exit':
            break

        row, col, row1, col1 = parse_coords(command)

        if (row1 == 0 or row1 == 7) and type(board.get_piece(row, col)) is Pawn:
            print("Введите символ для превращения пешки")
            print("Q - королева")
            print("R - ладья")
            print("N - конь")
            print("B - слон")
            symbol = input()
            board.move_and_promote_pawn(row, col, row1, col1, symbol)

        elif board.move_piece(row, col, row1, col1):
            print('Ход успешен')
            if not (board.Can_king_move(board.color)) and not (board.Piece_can_save_king(board.color)):
                print_board(board)
                if opponent(board.color==WHITE):
                    print("Выйграли БЕЛЫЕ")
                else:
                    print("Выйграли ЧЕРНЫЕ")
                return 0
        else:
            print('Координаты некорректы! Попробуйте другой ход!')

#Запуск программы
if __name__ == "__main__":
    main()