from Helper import read_input

input = read_input('InputDay18.txt')


class Token:
    KIND_NUMBER = 1
    KIND_PAREN_OPEN = 2
    KIND_PAREN_CLOSE = 3
    KIND_MULT = 4
    KIND_ADD = 5

    def __init__(self, kind, value=None):
        self.kind = kind
        self.value = value


def parse_number(expr):
    result = ''
    i = 0
    while i < len(expr) and expr[i].isdigit():
        result = result + expr[i]
        i += 1

    return int(result), i


def tokenize(expr):
    index = 0
    tokens = []
    paren_count = 0
    while index < len(expr):
        if expr[index].isdigit():
            number, advance = parse_number(expr[index:])
            index += advance
            tokens.append(Token(Token.KIND_NUMBER, number))
            continue
        elif expr[index] == '(':
            paren_count += 1
            tokens.append(Token(Token.KIND_PAREN_OPEN))
        elif expr[index] == ')':
            if paren_count == 0:
                raise Exception('Unmatched parenthesis; found excess at index {}'.format(index))
            paren_count -= 1
            tokens.append(Token(Token.KIND_PAREN_CLOSE))
        elif expr[index] == '*':
            tokens.append(Token(Token.KIND_MULT))
        elif expr[index] == '+':
            tokens.append(Token(Token.KIND_ADD))
        index += 1
    if paren_count > 0:
        raise Exception('Unmatched opening parenthesis.')
    return tokens


class Node:
    def __init__(self):
        self.nodes = []


def parse_op(tokens, index=0):
    node = Node()
    while index < len(tokens):
        if tokens[index].kind == Token.KIND_PAREN_OPEN:
            sub_node, new_index = parse_op(tokens, index + 1)
            node.nodes.append(sub_node.nodes)
            index = new_index
            continue
        elif tokens[index].kind == Token.KIND_PAREN_CLOSE:
            return node, index + 1
        elif tokens[index].kind == Token.KIND_NUMBER:
            node.nodes.append(tokens[index].value)
        elif tokens[index].kind == Token.KIND_MULT:
            node.nodes.append('*')
        elif tokens[index].kind == Token.KIND_ADD:
            node.nodes.append('+')
        index += 1
    return node, index


def patch_precedence(parsed):
    index = 0
    while index < len(parsed):
        if isinstance(parsed[index], list):
            parsed[index] = patch_precedence(parsed[index])
        elif parsed[index] == '+':
            rhs = patch_precedence(parsed[index + 1]) \
                if isinstance(parsed[index + 1], list) else parsed[index + 1]
            sub = [parsed[index - 1], parsed[index], rhs]
            parsed[index - 1] = sub
            parsed.pop(index)
            parsed.pop(index)
            continue
        index += 1
    return parsed


def parse(tokens):
    parsed, _ = parse_op(tokens)
    patched = patch_precedence(parsed.nodes)
    return patched


def evaluate_expression(expr):
    result = None
    last_op = None
    index = 0
    while index < len(expr):
        if not result:
            result = evaluate_expression(expr[index]) \
                if isinstance(expr[index], list) else expr[index]
        elif expr[index] == '+' or expr[index] == '*':
            last_op = expr[index]
        elif isinstance(expr[index], list):
            if last_op == '+':
                result += evaluate_expression(expr[index])
            elif last_op == '*':
                result *= evaluate_expression(expr[index])
        else:
            if last_op == '+':
                result += expr[index]
            elif last_op == '*':
                result *= expr[index]
        index += 1
    return result


def evaluate_language(expr):
    tokens = tokenize(expr)
    parsed = parse(tokens)
    return evaluate_expression(parsed)


sum = 0
for line in input:
    result = evaluate_language(line)
    sum += result
print(sum)
