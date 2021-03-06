WHITE = 1
BLACK = 2

'''Дополнительные методы'''
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

'''Классы фигур'''
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
        #Внизеяя
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

    def promotion(self, row, col, row1, col1, char):
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
            new_pawn = None
            return True
        return False

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

    def move_piece(self, row, col, row1, col1, *char):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт 'Ход успешен'.
        Если нет --- вернёт соотвествующую ошибку"""
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return 'Координаты не корректны'
        if row == row1 and col == col1:
            return 'Нельзя пойти в ту же клетку'

        piece = self.field[row][col]
        if piece is None:
            return 'Нужно ходить фигурой'
        if piece.get_color() != self.color:
            return 'Нельзя ходить фигурой противника'
        if row1 in {0, 7}:
            if col1 == 2 and self.castling0():
                self.field[row][2], self.field[row][4] = self.field[row][4], self.field[row][2]
                self.field[row][0], self.field[row][3] = self.field[row][3], self.field[row][0]
                self.get_piece(row, 2).not_move = False
                self.get_piece(row, 3).not_move = False
                self.color = opponent(self.color)
                return 'Дальняя рокировка успешна'
            elif col1 == 6 and self.castling7():
                self.field[row][6], self.field[row][4] = self.field[row][4], self.field[row][6]
                self.field[row][7], self.field[row][5] = self.field[row][5], self.field[row][7]
                self.get_piece(row, 6).not_move = False
                self.get_piece(row, 5).not_move = False
                self.color = opponent(self.color)
                return 'Ближняя рокировка успешна'
        if type(self.get_piece(row, col)) == Pawn and \
                (row == 6 and row1 == 7 and piece.get_color(row, col) == WHITE or
                 row == 1 and row1 == 0 and piece.get_color(row, col) == BLACK) and\
                self.promotion(row, col, row1, col1, char):
            return 'Ход успешен'
        if not piece.can_move(self, row, col, row1, col1):
            return 'Эта фигура не может ходить в это место'

        if type(piece) in {King, Rook}:
            piece.not_move = False
        elif type(piece) == Pawn:
            # взятие а проходе
            if self.get_piece(row1, col1) is None:
                if self.color == WHITE:
                    self.field[row1 - 1][col1] = None
                elif self.color == BLACK:
                    self.field[row1 + 1][col1] = None

        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        if type(piece) in {King, Rook}:
            piece.not_move = False
        elif type(piece) == Pawn:
            piece.freshly_two_move = abs(row - row1) == 2
        self.color = opponent(self.color)
        return 'Ход успешен'
    
    def is_under_attack(self, row, col, color):
        """Возращает True, если поле с координатами (row, col)
         находится под боем хотя бы одной фигуры цвета color."""
        for i in range(len(self.field)):
            for j, piece in enumerate(self.field[i]):
                if piece is not None and piece.get_color() == color and\
                   piece.can_move(self, i, j, row, col):
                    return True
        else:
            return False

    def find_king(self, color):
        for i in range(8):
            for j in range(8):
                if self.get_piece(i, j) == King(color):
                    return i, j
    
    def castling0(self):
        """Если дальняя рокировка возможна, программаа вернёт True, если нет — вернёт False."""
        if self.color == WHITE:
            row = 0
        else:
            row = 7

        if self.get_piece(row, 4) == King(self.color) and self.get_piece(row, 4).not_move and\
           self.get_piece(row, 0) == Rook(self.color) and self.get_piece(row, 0).not_move:
            # проверяем клетки между лодьёй и королём
            if self.is_under_attack(row, 4, opponent(self.color)):
                return False
            if self.get_piece(row, 1) is not None:
                return False
            for i in range(2, 4):
                if self.get_piece(row, i) is not None or\
                   self.is_under_attack(row, i, opponent(self.color)):
                    return False
            return True
        return False

    def castling7(self):
        """Если ближняя рокировка возможна, программаа вернёт True, если нет — вернёт False."""
        if self.color == WHITE:
            row = 0
        else:
            row = 7

        if self.get_piece(row, 4) == King(self.color) and self.get_piece(row, 4).not_move and\
           self.get_piece(row, 7) == Rook(self.color) and self.get_piece(row, 7).not_move:
            # проверяем клетки между лодьёй и королём
            if self.is_under_attack(row, 4, opponent(self.color)):
                return False
            for i in range(5, 7):
                if self.get_piece(row, i) is not None or\
                   self.is_under_attack(row, i, opponent(self.color)):
                    return False
            return True
        return False

    def checkmate(self):
        """Возращает True, если королю поставлен мат, иначе False."""
        color = self.color
        row, col = self.find_king(color)
        king = self.get_piece(row, col)

        if king.can_move_at_all(self, row, col):
            return False
        else:
            # поиск угрожающих фигур и своих фигур
            list_of_threatening_pieces = []
            list_of_my_pieces = []
            for i in range(8):
                for j, piece in enumerate(self.field[i]):
                    if piece is not None:
                        if piece.get_color() == color:
                            list_of_my_pieces.append((piece, i, j))
                        elif piece.get_color() == opponent(color) and \
                                piece.can_move(self, i, j, row, col):
                            list_of_threatening_pieces.append((piece, i, j))

            # если зажали в тиски
            if len(list_of_threatening_pieces) == 0:
                for piece, i, j in list_of_my_pieces:
                    if piece.can_move_at_all(self, i, j):
                        return False
                print("ПАТ")
                exit()

            elif len(list_of_threatening_pieces) == 1:
                # ищем, как закрыть от удара короля
                threatening_piece, row_coor, col_coor = list_of_threatening_pieces[0]

                if type(threatening_piece) in {Knight, Pawn}:
                    # если угрожает конь или пешка, то их можно только съесть
                    for piece, i, j in list_of_my_pieces:
                        if piece.can_move(self, i, j, row_coor, col_coor):
                            return False
                else:
                    # если угрожает слон, лодья или ферзь
                    # то определяем, откуда угрожают
                    dir_row = 0
                    dir_col = 0
                    in_cycle = abs(col_coor - col) + 1
                    if abs(row - row_coor) == abs(col - col_coor):
                        # если по диагонали
                        dir_col = abs(col_coor - col) // (col_coor - col)
                        dir_row = abs(row_coor - row) // (row_coor - row)
                    elif row == row_coor:
                        # если по горизонтали
                        dir_col = abs(col_coor - col) // (col_coor - col)
                        dir_row = 0
                    elif col == col_coor:
                        # если по вертикали
                        dir_col = 0
                        dir_row = abs(row_coor - row) // (row_coor - row)
                        in_cycle = abs(row_coor - row) + 1
                    # ищем фигуру, которая может встать между королём и угрожающей фигурой
                    for bet in range(1, in_cycle):
                        for piece, i, j in list_of_my_pieces:
                            if piece.can_move(self, i, j, row + dir_row * bet, col + dir_col * bet):
                                return False

            # если угрожающих фигур больше 1
            # или нельзя ходить ничем никуда
            # или нельзя съесть угрожающую фигуру
            # или нелья встать между угрожающей фигурой и королём
            self.winner = opponent(col)
            return True

        
class Piece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_moved(self):
        self.moved = True
        
    def is_moved(self):
        return self.moved

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

        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

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
        if (row == row1 or col == col1):
            return False

        if (abs(row1 - row) + abs(col1 - col) == 3):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

class King(Piece):
    '''Класс короля'''
    def char(self):
        return 'K'

    
    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1):
            return False
        if abs(row1 - row) > 1 or abs(col1 - col) > 1:
            return False  # если разница между клетками больше 1

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

class Bishop(Piece):
    '''Класс слона'''
    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        if (row == row1 or col == col1):
            return False
        # в ходе по диагонали
        # смещение по горизонтали == смещению по вертикали
        if (abs(row - row1) != abs(col - col1)):
            return False

        step_row = 1 if (row1 >= row) else -1
        step_col = 1 if (col1 >= col) else -1
        for r, c in zip(range(row + step_row, row1, step_row),
                        range(col + step_col, col1, step_col)):
            # Если на пути по диагонали есть фигура
            if not (board.get_piece(r, c) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

class Queen(Piece):
    '''Класс ферзя'''
    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        if board.get_piece(row1, col1) and board.get_piece(row1, col1).get_color() == self.color:
            return False

        xr = abs(row1 - row)  # разница между рядами
        xc = abs(col1 - col)  # разница между столбцами
        if row1 != row and col1 != col and xc != xr:
            return False

        dx = 1 if row1 > row else -1 if row1 < row else 0  # Проверка, что на пути фигуры нет других фигур
        dy = 1 if col1 > col else -1 if col1 < col else 0
        x = row + dx
        y = col + dy
        while x != row1 or y != col1:
            if board.get_piece(x, y) is not None:
                return False
            x += dx
            y += dy
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

'''Главная функция, посредством которой запускается игра'''
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
            board.promotion(row, col, row1, col1, symbol)
        elif board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')

#Запуск программы
#status = input('НАЧАТЬ ИГРУ?  Y / N ')
#if status == 'Y':
 #   main()
#else:
 #   raise SystemExit

if __name__ == "__main__":
    main()