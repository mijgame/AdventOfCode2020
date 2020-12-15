input = [0, 3, 6]

turn = 0 + len(input)
target = 2020
history = list(input)

for index in range(turn, target):
    print('Last number spoken is {}'.format(history[-1]))
    if history[-1] not in history[len(input):]:
        print('Number never spoken before')
        history.append(0)
    else:
        for h in range(-len(history) + 1, 0):
            if history[h] == history[-1]:
                history.append(len(history) - 1 - abs(h + 1))
                print('Number spoken before, at index {}'.format(abs(h + 1)))
                break
print(history[-1])
