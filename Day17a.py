from Helper import read_input

input = read_input('InputDay17.txt')


class Space:
    def __init__(self):
        self.store = set()

    def load_input(self, lines):
        z = 0
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '#':
                    self.store.add((x, y, z))

    def mark_each_neighbour(self, coord, counters):
        cx, cy, cz = coord
        for x in [cx - 1, cx, cx + 1]:
            for y in [cy - 1, cy, cy + 1]:
                for z in [cz - 1, cz, cz + 1]:
                    neighbour = (x, y, z)
                    if neighbour != coord:
                        if neighbour not in counters:
                            counters[neighbour] = 1
                        else:
                            counters[neighbour] += 1

    def count_active(self):
        return len(self.store)

    def run_cycle(self):
        counters = {}
        new_store = set()

        for coord in self.store:
            self.mark_each_neighbour(coord, counters)

        for coord, count in counters.items():
            if coord in self.store:
                if count == 2 or count == 3:
                    new_store.add(coord)
            else:
                if count == 3:
                    new_store.add(coord)

        self.store = new_store


space = Space()
space.load_input(input)

for i in range(6):
    space.run_cycle()

print(space.count_active())
