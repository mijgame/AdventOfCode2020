from Helper import read_input

input = read_input('InputDay12.txt')
for i in range(len(input)):
    input[i] = (input[i][0], int(input[i][1:]))

pos = [0, 0]
rotation = 0

for instr, arg in input:
    if instr == 'N':
        pos[1] += arg
    elif instr == 'S':
        pos[1] -= arg
    elif instr == 'E':
        pos[0] += arg
    elif instr == 'W':
        pos[0] -= arg
    elif instr == 'L':
        rotation -= arg
        rotation %= 360
    elif instr == 'R':
        rotation += arg
        rotation %= 360
    elif instr == 'F':
        if rotation == 0:
            pos[0] += arg
        elif rotation == 90:
            pos[1] -= arg
        elif rotation == 180:
            pos[0] -= arg
        elif rotation == 270:
            pos[1] += arg

print(abs(pos[0]) + abs(pos[1]))

