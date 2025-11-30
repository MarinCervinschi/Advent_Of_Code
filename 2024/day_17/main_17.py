import re

class Solution:

    def __init__(self, registers, program):
        self.program = program
        self.registers = registers
        self.pointer = 1
        self.std_out = []
        self.combo_operand = {
            0 : 0,
            1 : 1,
            2 : 2,
            3 : 3,
            4 : lambda: self.registers['A'],
            5 : lambda: self.registers['B'],
            6 : lambda: self.registers['C'],
        }
        self.instructions = {
            0 : self.adv,
            1 : self.bxl,
            2 : self.bst,
            3 : self.jnz,
            4 : self.bxc,
            5 : self.out,
            6 : self.bdv,
            7 : self.cdv,
        }
        
    def get_combo(self, operand):
        return self.combo_operand[operand]() if callable(self.combo_operand[operand]) else self.combo_operand[operand]

    def adv(self, operand):
        self.registers['A'] = self.registers['A'] // 2**self.get_combo(operand)
        self.pointer += 2

    def bxl(self, operand):
        self.registers['B'] ^= operand
        self.pointer += 2

    def bst(self, operand):
        self.registers['B'] = self.get_combo(operand) % 8
        self.pointer += 2

    def jnz(self, operand):
        if self.registers['A'] == 0:
            self.pointer += 2
        else:
            self.pointer = 1

    def bxc(self, operand):
        self.registers['B'] ^= self.registers['C']
        self.pointer += 2

    def out(self, operand):
        self.std_out.append(self.get_combo(operand) % 8)
        self.pointer += 2

    def bdv(self, operand):
        self.registers['B'] = self.registers['A'] // 2**self.get_combo(operand)
        self.pointer += 2

    def cdv(self, operand):
        self.registers['C'] = self.registers['A'] // 2**self.get_combo(operand)
        self.pointer += 2

    def part_1(self):
        
        while self.pointer < len(self.program):
            operand = self.program[self.pointer]
            self.instructions[self.program[self.pointer - 1]](operand)

        return self.std_out

    def part_2(self):
        def reset(A):
            self.registers['A'] = A
            self.registers['B'] = 0
            self.registers['C'] = 0
            self.pointer = 1
            self.std_out = []

        from collections import deque

        candidates = deque([0])
        min_candidate = 2 ** (3 * (len(program) - 1))

        while candidates and candidates[-1] < min_candidate:
            seed = candidates.popleft()
            for a in range(2 ** 6):
                a += seed << 6
                reset(A=a)
                out = self.part_1()
                if a < 8:
                    out.insert(0, 0)
                if out == program[-(len(out)):]:
                    candidates.append(a)
                if out == program:
                    break

        return candidates.pop()

if __name__ == '__main__':

    with open('puzzle.txt') as f:
        A, B, C, *program = (int(x) for x in re.findall(r'\d+', f.read()))

        registers = {
            'A' : A,
            'B' : B,
            'C' : C
        }
        sol = Solution(registers, program)

        print("Part 1 Output:", ','.join(map(str, sol.part_1())))
        print("Part 2 Output:", sol.part_2())