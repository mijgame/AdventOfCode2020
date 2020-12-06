from Helper import read_input_split_by

input = [group.split('\n') for group in read_input_split_by('Inputday6.txt', '\n\n')]

total_sum = 0
for group in input:
    letters = {}
    for i in range(26):
        letters[chr(ord('a') + i)] = False

    for member in group:
        for letter in member:
            letters[letter] = True

    total_sum += sum(letter == True for letter in letters.values())

print(total_sum)
