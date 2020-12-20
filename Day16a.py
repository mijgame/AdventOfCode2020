from Helper import read_input

input = read_input('InputDay16.txt')


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


def check_ticket(ticket, rules):
    for value in ticket:
        valid = 0
        for rule in rules:
            if rule[0] <= value <= rule[1]:
                valid += 1
        if 0 == valid:
            return False, value
    return True, 0


error_rate = 0
for ticket in other_tickets:
    valid, error = check_ticket(ticket, all_ranges)
    if not valid:
        error_rate += error

print(error_rate)
