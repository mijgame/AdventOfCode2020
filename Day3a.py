from Helper import read_input

map = read_input('InputDay3.txt')
print(map)

map_width = len(map[0])
x, y = 0, 0
trees = 0


def check_position(x, y):
    real_x = x % map_width

    if map[y][real_x] == '#':
        return 1

    return 0


while True:
    x += 3
    y += 1

    if y == len(map):
        break

    trees += check_position(x, y)

print(trees)
