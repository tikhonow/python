class Piece:  # Класс, от которого наследуются все фигуры
    def __init__(self, row, col, color):  # Определение координат фигуры и цвета
        self.row = row
        self.col = col
        self.color = color

    def change_position(self, row, col):  # Переопределение координат фигуры
        self.row = row
        self.col = col

    def get_color(self):  # Метод возвращает цвет фигуры
        return self.color


self.field[row][col] = None  # Снять фигуру.
self.field[row1][col1] = piece  # Поставить на новое место.
piece.change_position(row1, col1)  # Обновляем позицию фигуры.
self.color = opponent(self.color)  # Инверсируем цвет.
return True