def read_input(filename, cast=None):
    input = []
    with open(filename) as input_file:
        for line in input_file.readlines():
            if cast is not None:
                if cast == 'int':
                    input.append(int(line.strip()))
            else:
                input.append(line.strip())

    if [] == input[-1] or input[-1] is None:
        input.pop()

    return input


def read_input_split_by(filename, delimiter):
    with open(filename) as input_file:
        all_lines = input_file.read()
        input = all_lines.split(delimiter)
    return input
