from Helper import read_input
import parse

input = read_input('InputDay2.txt')
format = '{}-{} {}: {}'
valid = 0

for line in input:
    pos1, pos2, letter, input = parse.parse(format, line)

    # Convert to index
    pos1 = int(pos1) - 1
    pos2 = int(pos2) - 1

    if input[pos1] == letter or input[pos2] == letter:
        if input[pos1] == input[pos2]:
            continue
        valid += 1

print(valid)