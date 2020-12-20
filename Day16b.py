from Helper import read_input
import math

input = read_input('InputDay16.txt')
#
# input = [
#     'class: 0-1 or 4-19',
#     'row: 0-5 or 8-19',
#     'seat: 0-13 or 16-19',
#     '',
#     'your ticket:',
#     '11,12,13',
#     '',
#     'nearby tickets:',
#     '3,9,18',
#     '15,1,5',
#     '5,14,9',
# ]


def parse_rules(input):
    rules = []
    for item in input:
        name, cond = item.split(':')
        r1, r2 = cond.split(' or ')
        rules.append(
            (name, [int(i) for i in r1.split('-')], [int(i) for i in r2.split('-')],)
        )
    return rules


def parse_tickets(input):
    tickets = []
    for line in input[1:]:
        tickets.append([int(i) for i in line.split(',')])
    return tickets


segments = []
index = 0
for line in input:
    if index == len(segments):
        segments.append([])
    if '' == line:
        index += 1
        continue
    segments[index].append(line)

rules = parse_rules(segments[0])
your_ticket = parse_tickets(segments[1])[0]
other_tickets = parse_tickets(segments[2])

all_ranges = []
for rule in rules:
    all_ranges.append(rule[1])
    all_ranges.append(rule[2])


def check_bounds(value, bounds):
    return bounds[0] <= value <= bounds[1]


def check_ticket(ticket, rules):
    for value in ticket:
        valid = 0
        for rule in rules:
            if check_bounds(value, rule):
                valid += 1
        if 0 == valid:
            return False, value
    return True, 0


def guess_rule(column, rules):
    matching = []
    for rule in rules:
        matches = True
        for value in column:
            if not check_bounds(value, rule[1]) and not check_bounds(value, rule[2]):
                matches = False
                break
        if matches:
            matching.append(rule)
    return matching


valid_tickets = []
for ticket in other_tickets:
    valid, error = check_ticket(ticket, all_ranges)
    if valid:
        valid_tickets.append(ticket)

available_rules = list(rules)
matches = []
while len(available_rules) > 0:
    for col in range(len(valid_tickets[0])):
        column = [ticket[col] for ticket in valid_tickets]
        options = guess_rule(column, available_rules)
        if len(options) == 1:
            matches.append((col, options[0]))
            available_rules.remove(options[0])

fields_to_check = [field[0] for field in matches if field[1][0].startswith('departure')]
result = math.prod([your_ticket[field] for field in fields_to_check])
print(result)
