from Chess import Board, Piece, Rook, Pawn, Knight, Bishop, Queen, King, WHITE, BLACK


def main():
    print("Пример 1",'\n')
    board = Board()
    board.field = [([None] * 8) for i in range(8)]
    board.field[0][3] = Queen(WHITE)
    queen = board.get_piece(0, 3)
    for row in range(7, -1, -1):
        for col in range(8):
            if queen.can_move(board, 0, 3, row, col):
                print('x', end=' ')
            else:
                cell = board.cell(row, col)[1]
                cell = cell if cell != ' ' else '-'
                print(cell, end=' ')
        print()
    print("Пример 2",'\n')
    row0 = 4
    col0 = 5

    board = Board()
    board.field = [([None] * 8) for i in range(8)]
    board.field[row0][col0] = Bishop(BLACK)
    bishop = board.get_piece(row0, col0)

    for row in range(7, -1, -1):
        for col in range(8):
            if bishop.can_move(board, row0, col0, row, col):
                print('x', end=' ')
            else:
                cell = board.cell(row, col)[1]
                cell = cell if cell != ' ' else '-'
                print(cell, end=' ')
        print()
    print("Пример 3",'\n')
    row0 = 2
    col0 = 2
    knight = Knight(WHITE)
    board = Board()
    for row in range(7, -1, -1):
        for col in range(8):
            if row == row0 and col == col0:
                print(knight.char(), end=' ')
            elif knight.can_move(board, row0, col0, row, col):
                print('x', end=' ')
            else:
                print('-', end=' ')
        print()

if __name__ == "__main__":
    main()