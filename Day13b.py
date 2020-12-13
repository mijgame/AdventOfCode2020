from Helper import read_input
import math

input = read_input('InputDay13.txt')

busses = [(b if b == 'x' else int(b)) for b in input[1].split(',')]


def check_valid(schedule, value, index=0):
    if index == len(schedule) - 1:
        return True, index

    _, offset = schedule[index]
    if (value + offset) % schedule[index + 1][0] != 0:
        return False, index
    return check_valid(schedule, value + offset, index + 1)


def make_offset_tuples(schedule):
    result = []
    offset = 1
    for i in reversed(schedule):
        if i == 'x':
            offset += 1
        else:
            result.append((i, offset))
            offset = 1
    result.reverse()
    return result


def get_first_timestamp(schedule):
    schedule = make_offset_tuples(schedule)
    bus, _ = schedule[0]
    next_bus, _ = schedule[1]
    value = bus
    while True:
        result, index = check_valid(schedule, value)
        if result:
            return value
        value += math.prod([s[0] for s in schedule[:index + 1]])


print(get_first_timestamp(busses))
