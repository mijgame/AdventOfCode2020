from Helper import read_input
import parse

input = read_input('InputDay2.txt')
format = '{}-{} {}: {}'
valid = 0

for line in input:
    lower_bound, upper_bound, letter, input = parse.parse(format, line)
    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)

    letter_count = len([x for x in input if x == letter])
    if letter_count >= lower_bound and letter_count <= upper_bound:
        valid += 1

print(valid)