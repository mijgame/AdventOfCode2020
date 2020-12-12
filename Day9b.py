from Helper import read_input

input = read_input('InputDay9.txt', 'int')


def check_slice(slice, find):
    for i in slice:
        for j in slice:
            if i + j == find:
                return i, j
    return None


def find_inconsistent_number(input, preamble, consider):
    index = preamble
    end = len(input)

    while index < end:
        slice = input[index - consider:index]
        find = input[index]

        if check_slice(slice, find) is None:
            return find
        index += 1

    return None


def find_contiguous_range(input, target):
    current = 0
    to = current + 2

    end = len(input)

    while current < end:
        range_sum = sum(input[current:to - current])
        if range_sum == target:
            return input[current:to - current]
        elif range_sum > target:
            current += 1
            to = current + 2
        else:
            to += 1

    return None


inconsistent_number = find_inconsistent_number(input, 25, 25)
range = find_contiguous_range(input, inconsistent_number)
print(range)
print(min(range) + max(range))
