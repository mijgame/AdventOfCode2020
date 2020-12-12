from Helper import read_input

input = sorted(read_input('InputDay10.txt', 'int'))
input.insert(0, 0)
input.append(input[-1] + 3)


def dfs(input, index=0, visited=None, cache=None):
    if cache is None:
        cache = {}

    if index == len(input) - 1:
        return 1
    if visited is None:
        visited = set()
    if index not in visited:
        visited.add(index)
        count = 0
        j = index + 1
        while j < len(input) and input[j] - input[index] <= 3:
            if j not in cache:
                cache[j] = dfs(input, j, visited, cache)
            count += cache[j]
            j += 1
        visited.remove(index)
        return count
    return 0


print(dfs(input))
