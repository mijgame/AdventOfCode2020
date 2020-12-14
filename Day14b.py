from Helper import read_input

input = read_input('InputDay14.txt')


def get_operation(line: str):
    if line.startswith('mask'):
        return 'mask', line[7:], None
    else:
        return 'mem', int(line[4:line.find(']')]), int(line[line.find('=') + 1:])


def generate_addresses(mask: str, value, enforce=None, index=0):
    if enforce is None:
        enforce = int(mask.replace('1', '0').replace('X', '1'), 2)
    if index == len(mask):
        value = (value & (~enforce)) | int(mask, 2)
        yield value
    elif mask[index] == 'X':
        l = list(mask)
        l[index] = '1'
        yield from generate_addresses(''.join(l), value, enforce, index + 1)
        l[index] = '0'
        yield from generate_addresses(''.join(l), value, enforce, index + 1)
    else:
        yield from generate_addresses(mask, value, enforce, index + 1)


memory = {}
mask = ''
for line in input:
    instruction, arg1, arg2 = get_operation(line)

    if instruction == 'mask':
        mask = arg1
    else:
        count = 0
        for address in generate_addresses(mask, arg1):
            memory[address] = arg2
            count += 1

print(sum(memory.values()))
