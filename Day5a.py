from Helper import read_input

input = read_input('InputDay5.txt')


def approach(start, end, lower, upper, line):
    range = (start, end)
    for char in line:
        diff = range[1] - range[0]
        if char == lower:
            range = (range[0], range[0] + diff // 2)
        elif char == upper:
            range = (range[0] + diff // 2 + 1, range[1])
        else:
            print("Unknown char {} in line".format(char))
    return range[0]


highest_seat_id = 0

for line in input:
    row = approach(0, 127, 'F', 'B', line[:7])
    column = approach(0, 7, 'L', 'R', line[7:])
    seat_id = row * 8 + column

    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print(highest_seat_id)
