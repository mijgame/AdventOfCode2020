from Helper import read_input

input = read_input('InputDay11.txt')


def run_diagonal(layout, x_range, y_range, result):
    x_range = iter(x_range)
    y_range = iter(y_range)

    while True:
        x = next(x_range, None)
        y = next(y_range, None)

        if x is None or y is None:
            return
        if layout[y][x] != '.':
            result.append(layout[y][x])
            return


def get_adjacency(layout, row, seat):
    result = []

    not_hugging_left = seat > 0
    not_hugging_right = seat != len(layout[0]) - 1
    not_top_row = row > 0
    not_bottom_row = row != len(layout) - 1

    range_seat_right_side = range(seat + 1, len(layout[0]))
    range_seat_left_side = list(reversed(range(seat)))
    range_seat_below = range(row + 1, len(layout))
    range_seat_above = list(reversed(range(row)))

    # Horizontal
    if not_hugging_right:
        for i in range_seat_right_side:
            if layout[row][i] != '.':
                result.append(layout[row][i])
                break

    if not_hugging_left:
        for i in range_seat_left_side:
            if layout[row][i] != '.':
                result.append(layout[row][i])
                break

    # Vertical
    if not_bottom_row:
        for i in range_seat_below:
            if layout[i][seat] != '.':
                result.append(layout[i][seat])
                break

    if not_top_row:
        for i in range_seat_above:
            if layout[i][seat] != '.':
                result.append(layout[i][seat])
                break

    # Diagonal
    if not_top_row and not_hugging_left:
        run_diagonal(layout, range_seat_left_side, range_seat_above, result)

    if not_top_row and not_hugging_right:
        run_diagonal(layout, range_seat_right_side, range_seat_above, result)

    if not_bottom_row and not_hugging_right:
        run_diagonal(layout, range_seat_right_side, range_seat_below, result)

    if not_bottom_row and not_hugging_left:
        run_diagonal(layout, range_seat_left_side, range_seat_below, result)

    return ''.join(result)


def iterate_layout(layout):
    new_layout = layout.copy()

    for row in range(len(layout)):
        for seat in range(len(layout[row])):
            if layout[row][seat] == 'L':
                if '#' not in get_adjacency(layout, row, seat):
                    r = list(new_layout[row])
                    r[seat] = '#'
                    new_layout[row] = ''.join(r)

            elif layout[row][seat] == '#':
                if get_adjacency(layout, row, seat).count('#') >= 5:
                    r = list(new_layout[row])
                    r[seat] = 'L'
                    new_layout[row] = ''.join(r)

    return new_layout


def layouts_equals(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


layout = input
changed = True
while changed:
    new_layout = iterate_layout(layout)
    changed = not layouts_equals(new_layout, layout)
    layout = new_layout

occupied_seats = 0
for row in layout:
    occupied_seats += row.count('#')
print(occupied_seats)
