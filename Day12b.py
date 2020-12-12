import math
from Helper import read_input

input = read_input('InputDay12.txt')
for i in range(len(input)):
    input[i] = (input[i][0], int(input[i][1:]))

# Start position as given
ship = [0, 0]
waypoint = [10, 1]


def to_polar(x, y):
    return math.sqrt(pow(x, 2) + pow(y, 2)), math.degrees(math.atan2(y, x))


def to_cartesian(r, theta):
    theta = math.radians(theta)
    return r * math.cos(theta), r * math.sin(theta)


for instr, arg in input:
    if instr == 'N':
        waypoint[1] += arg
    elif instr == 'S':
        waypoint[1] -= arg
    elif instr == 'E':
        waypoint[0] += arg
    elif instr == 'W':
        waypoint[0] -= arg
    elif instr == 'L' or instr == 'R':
        r, theta = to_polar(waypoint[0], waypoint[1])
        theta += -arg if instr == 'R' else arg
        theta %= 360
        cartesian = to_cartesian(r, theta)
        waypoint = [round(cartesian[0]), round(cartesian[1])]
    elif instr == 'F':
        ship[0] += arg * waypoint[0]
        ship[1] += arg * waypoint[1]

print(abs(ship[0]) + abs(ship[1]))
