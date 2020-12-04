from Helper import read_input_split_by
import re

input = read_input_split_by('InputDay4.txt', '\n\n')

# Remove newlines from values
for i in range(len(input)):
    input[i] = input[i].replace('\n', ' ')

# Parse input into dicts
passports = []
for line in input:
    passport = dict()

    for segment in line.split(' '):
        if '' == segment:
            continue

        field, value = segment.split(':')
        passport[field] = value
    passports.append(passport)

# Note missing 'cid'
colorRegex = re.compile('#[0-9a-f]{6}$')
numberRegex = re.compile('[0-9]{9}$')
lengthRegex = re.compile('([0-9]{2}|[0-9]{3})(cm|in)$')

def check_passport(passport):
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if field not in passport:
            return False

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    byr = int(passport['byr'])
    if byr < 1920 or byr > 2002:
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr = int(passport['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    eyr = int(passport['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False

    # hgt (Height) - a number followed by either cm or in:
    #  - If cm, the number must be at least 150 and at most 193.
    #  - If in, the number must be at least 59 and at most 76.
    match = lengthRegex.fullmatch(passport['hgt'])
    if match is None:
        return False
    else:
        length = int(match[1])
        unit = match[2]
        if unit == 'cm':
            if length < 150 or length > 193:
                return False
        elif unit == 'in':
            if length < 59 or length > 76:
                return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if colorRegex.match(passport['hcl']) is None:
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if numberRegex.match(passport['pid']) is None:
        return False

    # cid (Country ID) - ignored, missing or not.
    return True


validPassports = 0
for passport in passports:
    if check_passport(passport):
        validPassports += 1


print(validPassports)
