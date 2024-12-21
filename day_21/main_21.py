from itertools import permutations, product, combinations
from functools import lru_cache

class Solution:

    def __init__(self, codes):
        self.codes = codes
        self.directions = {
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1),
            "^": (-1, 0)
        }
        self.numeric_keypad = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "0": (3, 1),
            "A": (3, 2)
        }
        self.directional_keypad = {
            "^": (0, 1),
            "A": (0, 2),
            "<": (1, 0),
            "v": (1, 1),
            ">": (1, 2)
        }
    
    # -------------------------- Part 1 -------------------------- #
    def shortest_sequences(self, keypad, code):

        bests = []
        pos = keypad["A"]

        for c in code:
            next_pos = keypad[c]
            dx, dy = next_pos[0] - pos[0], next_pos[1] - pos[1]
            path = "v" * max(0, dx) + "^" * max(0, -dx) + ">" * max(0, dy) + "<" * max(0, -dy)
            
            rows = list(set(["".join(x) + "A" for x in permutations(path)]))
            combs = []
            for row in rows:
                x, y = pos
                for c in row[:-1]:
                    dx, dy = self.directions[c]
                    x, y = x + dx, y + dy
                    if not (x, y) in keypad.values():
                        break
                else:
                    combs.append(row)

            bests.append(combs)
            pos = next_pos
        
        return ["".join(x) for x in product(*bests)]
        

    def part_1(self):
        ans = 0
        for code in self.codes:
            door_codes = self.shortest_sequences(self.numeric_keypad, code)

            robot_one_codes = []
            for door_code in door_codes:
                robot_one_codes.extend(self.shortest_sequences(self.directional_keypad, door_code))
            
            robot_two_codes = []
            for robot_one_code in robot_one_codes:
                robot_two_codes.extend(self.shortest_sequences(self.directional_keypad, robot_one_code))

            best = min([len(x) for x in robot_two_codes])
            #print(best, int(code[:-1]))
            ans += best * int(code[:-1])
        
        print(f"Complexities part 1 --> {ans}")
        
    # -------------------------- Part 2 -------------------------- #      

    def get_combos(self, ca, a, cb, b):
        for idxs in combinations(range(a + b), r=a):
            res = [cb] * (a + b)
            for i in idxs:
                res[i] = ca
            yield "".join(res)         

    def generate_ways(self, a, b, keypad):
        keypad = self.directional_keypad if keypad else self.numeric_keypad

        pos = keypad[a]
        next_pos = keypad[b]
        dx = next_pos[0] - pos[0]
        dy = next_pos[1] - pos[1]

        path = []
        if dx > 0:
            path += ["v", dx]
        else:
            path += ["^", -dx]
        if dy > 0:
            path += [">", dy]
        else:
            path += ["<", -dy]
        
        rows = list(set(["".join(x) + "A" for x in self.get_combos(*path)]))
        combs = []
        for row in rows:
            x, y = pos
            for c in row[:-1]:
                dx, dy = self.directions[c]
                x, y = x + dx, y + dy
                if not (x, y) in keypad.values():
                    break
            else:
                combs.append(row)

        return combs
    
    @lru_cache(None)
    def get_cost(self, a, b, keypad, depth=0):
        if depth == 0:
            return min([len(x) for x in self.generate_ways(a, b, True)])

        ways = self.generate_ways(a, b, keypad)
        best_cost = 1 << 60
        for seq in ways:
            seq = "A" + seq
            cost = 0
            for i in range(len(seq)-1):
                a, b = seq[i], seq[i+1]
                cost += self.get_cost(a, b, True, depth-1)
            
            best_cost = min(best_cost, cost)
        
        return best_cost

    def part_2(self):
        ans = 0
        depth = 25
        for code in self.codes:
            code = "A" + code
            cost = 0
            for i in range(len(code)-1):
                a, b = code[i], code[i+1]
                cost += self.get_cost(a, b, False, depth)
            
            ans += cost * int(code[1:-1])

        print(f"Complexities part 2 --> {ans}")


if __name__ == '__main__':
    with open('puzzle.txt') as f:
        codes = [row.strip() for row in f]

        sol = Solution(codes)
        sol.part_1(), sol.part_2()