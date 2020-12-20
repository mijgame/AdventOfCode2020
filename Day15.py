input = [1, 2, 16, 19, 18, 0]

turn = 0 + len(input)

# Change to 2020 for 15a
target = 30000000

positions = {}


def add_pos(number, position):
    if number not in positions:
        positions[number] = [position]
    else:
        positions[number].append(position)


for i in range(len(input)):
    add_pos(input[i], i)

# print(positions)
history = list(input)

for index in range(turn, target):
    # print('Turn ' + str(curr_turn))
    # print(history[-1], history[:len(history) - 1], positions)
    last_number = history[-1]
    # print('Last number was ' + str(last_number))
    if last_number not in positions or 1 == len(positions[last_number]):
        # print('Number not spoken before')
        add_pos(0, len(history))
        history.append(0)
    else:
        last_turn = positions[last_number][-1] + 1
        turn_before_that = positions[last_number][-2] + 1
        # print('Last turn was ' + str(last_turn))
        # print('Turn before that was ' + str(turn_before_that))
        # print('Spoke ' + str(last_turn - turn_before_that))
        history.append(last_turn - turn_before_that)
        add_pos(last_turn - turn_before_that, len(history) - 1)

print(history[-1])
