from Helper import read_input

input = read_input('InputDay13.txt')

depart = int(input[0])
busses = [int(b) for b in input[1].split(',') if b != 'x']

differences = {}
for bus in busses:
    if depart % bus == 0:
        differences[bus] = 0
    else:
        differences[bus] = (depart // bus * bus + bus) - depart

bus = min(differences, key=differences.get)
print(bus * differences[bus])
