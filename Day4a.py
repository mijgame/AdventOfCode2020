from Helper import read_input_split_by

input = read_input_split_by('InputDay4.txt', '\n\n')

# Remove newlines from values
for i in range(len(input)):
    input[i] = input[i].replace('\n', ' ')

# Parse input into dicts
passports = []
for line in input:
    passport = dict()

    if '' == line:
        continue

    for segment in line.split(' '):
        if '' == segment:
            continue

        field, value = segment.split(':')
        passport[field] = value

    passports.append(passport)

# Note missing 'cid'
requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validPassports = 0

for passport in passports:
    valid = True
    for field in requiredFields:
        if field not in passport:
            valid = False
            break

    if valid:
        validPassports += 1

print(validPassports)

