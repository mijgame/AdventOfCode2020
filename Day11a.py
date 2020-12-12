from Helper import read_input

input = read_input('InputDay11.txt')


def get_adjacency(layout, row, seat):
    result = ''

    # Row above
    if row > 0:
        if seat > 0:
            result += layout[row - 1][seat - 1]
        if seat < len(layout[0]) - 1:
            result += layout[row - 1][seat + 1]
        result += layout[row - 1][seat]

    # Same row
    if seat > 0:
        result += layout[row][seat - 1]
    if seat < len(layout[0]) - 1:
        result += layout[row][seat + 1]

    # Bottom row
    if row < len(layout) - 1:
        if seat > 0:
            result += layout[row + 1][seat - 1]
        if seat < len(layout[0]) - 1:
            result += layout[row + 1][seat + 1]
        result += layout[row + 1][seat]
    return result


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
                if get_adjacency(layout, row, seat).count('#') >= 4:
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
