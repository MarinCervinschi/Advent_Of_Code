
def isIncreasing(line):
    for i in range(len(line) - 1):
        if line[i] - line[i + 1] > 0:
            return False
    return True

def isDecreasing(line):
    for i in range(len(line) - 1):
        if line[i] - line[i + 1] < 0:
            return False
    return True

def isValid(line):
    for i in range(len(line) - 1):
        diff = abs(line[i] - line[i + 1])
        if diff != 1 and diff != 2 and diff != 3:
            return False
    if not isIncreasing(line) and  not isDecreasing(line):
        return False
    return True

if __name__ == '__main__':

    with open('puzzle.txt') as f:
        # part 1
        safe = 0
        for line in f.read().split('\n'):
            line = [int(i) for i in line.split()]
            if isValid(line):
                safe += 1
            else:
                # part 2
                for i in range(len(line)):
                    erase = line[:i] + line[i+1:]
                    if isValid(erase):
                        safe += 1
                        break
        print(safe)
