from Helper import read_input

program = []
for line in read_input('InputDay8.txt'):
    instr, arg = line.split(' ')
    program.append((instr, int(arg)))


def switch(program, iptr):
    program[iptr] = ('nop' if program[iptr][0] == 'jmp' else 'jmp', program[iptr][1])
    return program


def run_program(program, iptr=0, acc=0, check=True):
    passed = set()
    while iptr < len(program):
        if iptr in passed:
            return -1
        passed.add(iptr)

        instr, arg = program[iptr]

        if 'acc' == instr:
            acc += arg
        else:
            if check:
                result = run_program(switch(program, iptr), iptr, acc, False)
                if result > -1:
                    return result
            if 'jmp' == instr:
                iptr += arg
                continue
        iptr += 1
    return acc


print(run_program(program))
