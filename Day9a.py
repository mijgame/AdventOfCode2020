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
        slice = input[index - preamble:index]
        find = input[index]

        if check_slice(slice, find) is None:
            return find
        index += 1

    return None


print(find_inconsistent_number(input, 25, 25))
