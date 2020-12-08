from Helper import read_input

program = []
for line in read_input('InputDay8.txt'):
    instr, arg = line.split(' ')
    program.append((instr, int(arg)))

acc = 0
iptr = 0

passed = set()
while iptr < len(program):
    if iptr in passed:
        break
    passed.add(iptr)
    instr, arg = program[iptr]

    if 'jmp' == instr:
        iptr += arg
        continue
    elif 'acc' == instr:
        acc += arg
    iptr += 1

print(acc)
