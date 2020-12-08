from Helper import read_input
import re

input = read_input('InputDay7.txt')

keyRegex = re.compile('(.+?) bags contain')
valueRegex = re.compile('(?:contain)? (\d+) (.+?) bags?')

bags = {}
possible = set('shiny gold')

for line in input:
    key = keyRegex.match(line)[1]
    values = valueRegex.findall(line)
    bags[key] = set([value[1] for value in values])


def check_bag_for(bag, search):
    for allowed in bags[bag]:
        if search in allowed:
            return True
    return False


while True:
    changed = False

    for bag in bags:
        if bag in possible:
            continue

        for p in set(possible):
            if check_bag_for(bag, p):
                possible.add(bag)
                changed = True

    if not changed:
        break

print(len(possible))
