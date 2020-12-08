from Helper import read_input
import re

input = read_input('InputDay7.txt')

keyRegex = re.compile('(.+?) bags contain')
valueRegex = re.compile('(?:contain)? (\d+) (.+?) bags?')


class Tree(object):
    def __init__(self, name='', count=0):
        self.children = []
        self.name = name
        self.count = count

    def __str__(self, level=0):
        ret = '{}[{}, {}]\n'.format('\t' * level, self.count, self.name)
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add(self, name, count):
        node = Tree()
        node.name = name
        node.count = count
        self.children.append(node)
        return node


bags = {}

for line in input:
    key = keyRegex.match(line)[1]
    values = valueRegex.findall(line)
    bags[key] = [(int(value[0]), value[1]) for value in values]


def descend(node, tree=None):
    count, name = node
    tree = tree.add(name, count) if tree else Tree(name, count)

    for required in bags[name]:
        descend(required, tree)
    return tree


def sum_tree_count(tree):
    if 0 == len(tree.children):
        return tree.count
    return tree.count + tree.count * sum([sum_tree_count(n) for n in tree.children])


def count_dependant_bags(tree):
    return sum_tree_count(tree) - 1  # - 1 for the root bag


print(count_dependant_bags(descend((1, 'shiny gold'))))
