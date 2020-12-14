from Helper import read_input

input = read_input('InputDay14.txt')


def get_operation(line: str):
    if line.startswith('mask'):
        return 'mask', line[7:], None
    else:
        return 'mem', int(line[4:line.find(']')]), int(line[line.find('=') + 1:])


memory = {}
and_mask = 0
or_mask = 0
for line in input:
    instruction, arg1, arg2 = get_operation(line)

    if instruction == 'mask':
        and_mask = int(arg1.replace('X', '1'), 2)
        or_mask = int(arg1.replace('X', '0'), 2)
    else:
        memory[arg1] = (arg2 & and_mask) | or_mask

print(sum(memory.values()))
