from Helper import read_input

input = read_input('InputDay1.txt', cast='int')

answer = 0
for outer in input:
    for inner in input:
        for moreInner in input:
            if 2020 == outer + inner + moreInner:
                answer = outer * inner * moreInner
                break

print(answer)