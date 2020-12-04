from Helper import read_input

map = read_input('InputDay3.txt')
map_width = len(map[0])


def check_position(x, y):
    real_x = x % map_width

    if map[y][real_x] == '#':
        return 1

    return 0


def check_slope(right, down):
    x, y = 0, 0
    trees = 0

    while True:
        x += right
        y += down

        if y >= len(map):
            break

        trees += check_position(x, y)
    return trees


s1 = check_slope(1, 1)
s2 = check_slope(3, 1)
s3 = check_slope(5, 1)
s4 = check_slope(7, 1)
s5 = check_slope(1, 2)

print(s1 * s2 * s3 * s4 * s5)
