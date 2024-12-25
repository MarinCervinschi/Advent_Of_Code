if __name__ == "__main__":

    with open("puzzle.txt") as f:
        locks = []
        keys = []

        lock, key = [], []

        for row in f:
            row = row.strip()
            if row and (row == '#####' or lock) and not key:
                lock.append(list(row))
            elif row and (row == '.....' or key) and not lock:
                key.append(list(row))
            else:
                if lock:
                    locks.append(lock)
                    lock = []
                elif key:
                    keys.append(key)
                    key = []


        def _print(m, c):
            for row in m:
                print(''.join(row))

            print(f"{3 * '-'}{c}{3 * '-'}")

        locks_heights = [[-1] * 5 for _ in range(len(locks))]
        keys_heights = [[-1] * 5 for _ in range(len(keys))]

        for i, lock in enumerate(locks):
            _print(lock, '🔒')
            for r in range(7):
                for c in range(5):
                    if lock[r][c] == '#':
                        locks_heights[i][c] += 1 
            
            print(locks_heights[i])
            print(8 * '-')

            
        for i, key in enumerate(keys):
            _print(key, '🔑')
            for r in range(7):
                for c in range(5):
                    if key[r][c] == '#':
                        keys_heights[i][c] += 1 
            print(keys_heights[i])
            print(8 * '-')


        fit = 0
        for lock_height in locks_heights:
            for key_height in keys_heights:
                try_fit = [a + b for a, b in zip(lock_height, key_height)]
                if all(t < 6 for t in try_fit):
                    fit += 1
        
        print(f"The number of unique lock/key pairs that fit together without overlapping in any column is {fit}")


                


        
        
       