
_cache = {'': 1}

def count_ways(design, towels):
    if design in _cache:
        return _cache[design]
    else:
        count = sum(count_ways(design[len(towel):], towels) for towel in towels if design.startswith(towel))
        _cache[design] = count
        return count

if __name__ == '__main__':
     with open('puzzle.txt') as f:
        patterns = []
        designs = []
        for row in f:
            row = row.strip()
            if row and not patterns:
                patterns = (list(row.split(',')))
            elif row:
                designs.append(row)

        towels = [pattern.strip() for pattern in patterns]
        ways = [count_ways(design, towels) for design in designs]
        print(len(ways) - ways.count(0))
        print(sum(ways))
