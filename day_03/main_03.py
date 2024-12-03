import re
if __name__ == '__main__':

    with open('puzzle.txt') as f:
        # part 1
        string = f.read()
        #string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        pattern = r'mul\((\d+),(\d+)\)'
        muls = re.findall(pattern, string)
        print(sum(int(mul[0]) * int(mul[1]) for mul in muls))
        
        # part 2
        filtered_text = re.sub(r"don't\(\).*?do\(\)", "", string, flags=re.DOTALL)
        muls = re.findall(pattern, filtered_text)

        print(muls)
        print(sum(int(mul[0]) * int(mul[1]) for mul in muls))
        