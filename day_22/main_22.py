from functools import cache

if __name__ == "__main__":

    with open("puzzle.txt") as f:
        puzzle = list(map(int, (row.strip() for row in f)))
        REPEAT_COUNT = 2000

        @cache
        def mix(num, value):
            return num ^ value

        @cache
        def prune(value):
            return value % 16777216
        
        @cache
        def _1(num):
            return prune(mix(num, num * 64))

        @cache
        def _2(num):
            return prune(mix(num, num // 32))
            
        @cache
        def _3(num):
            return prune(mix(num, num * 2048))
        
        def part_1():
            ans = 0
            for num in puzzle:
                price = num
                for _ in range(REPEAT_COUNT):
                    price = _1(price)
                    price = _2(price)
                    price = _3(price)
                ans += price

            return ans
            

        def part_2():
            seqs = set()

            @cache
            def get_dict(price):
                i = 0
                bananas = {}
                seq, diff = [], []
                for _ in range(REPEAT_COUNT):
                    banana = price % 10
                    seq.append(banana)
                    if len(seq) > 1:
                        diff.append((seq[-1] - seq[-2] ))

                    if len(diff) > 3:
                        sequence = tuple(diff[i:])
                        if bananas.get(sequence) is None:
                            bananas[sequence] = banana
                            seqs.add(sequence)
                        i += 1
                    price = _1(price)
                    price = _2(price)
                    price = _3(price)
                
                return bananas

            _map = [get_dict(num) for num in puzzle]
            return max([sum(i.get(seq, 0) for i in _map) for seq in seqs])

        print(f"Answer part 1 --> {part_1()}") # 12s
        print(f"Answer part 2 --> {part_2()}") # 33s