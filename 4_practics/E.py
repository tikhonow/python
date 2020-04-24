#E. Ход конем
def coord_to_tuple(coord) -> tuple:
    return ord(coord[0]) - ord('A') + 1, int(coord[1])


def coord_to_string(coord) -> str:
    return ''.join((chr(coord[0] + ord('A') - 1), str(coord[1])))


def isBoard(coord) -> bool:
    return all(map(lambda x: 0 < x < 9 , coord))


def list_of_turns(c) -> list:
    x, y = c
    cells = [(x + i, y + j) for j in range(-1, 2, 2) for i in range(-2, 3, 4) if isBoard((x + i, y + j))]
    cells.extend([(x + i, y + j) for j in range(-2, 3, 4) for i in range(-1, 2, 2) if isBoard((x + i, y + j))])
    return sorted([coord_to_string(i) for i in cells])

cell = coord_to_tuple(input())
print(list_of_turns(cell))
