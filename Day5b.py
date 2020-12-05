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


seats = []
for line in input:
    row = approach(0, 127, 'F', 'B', line[:7])
    column = approach(0, 7, 'L', 'R', line[7:])
    seat_id = row * 8 + column
    seats.append(seat_id)

seats.sort()

for i in range(len(seats) - 1):
    if seats[i+1] != seats[i] + 1:
        print(seats[i] + 1)
