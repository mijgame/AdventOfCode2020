from Helper import read_input

input = sorted(read_input('InputDay10.txt', 'int'))

input.insert(0, 0)
input.append(input[-1] + 3)

diffs = {}
for i in range(len(input) - 1):
    diff = input[i + 1] - input[i]

    if diff not in diffs:
        diffs[diff] = 1
    else:
        diffs[diff] += 1

print(diffs[1] * diffs[3])
