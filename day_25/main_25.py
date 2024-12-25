import os, time
from colorama import Fore, Style

if __name__ == "__main__":

    with open("puzzle.txt") as f:
        locks, keys = [], []
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

        locks_heights = [[-1] * 5 for _ in range(len(locks))]
        keys_heights = [[-1] * 5 for _ in range(len(keys))]

        for i, lock in enumerate(locks):
            for r in range(7):
                for c in range(5):
                    if lock[r][c] == '#':
                        locks_heights[i][c] += 1 
            
        for i, key in enumerate(keys):
            for r in range(7):
                for c in range(5):
                    if key[r][c] == '#':
                        keys_heights[i][c] += 1 

        def visulisation(lock, key, match=False):

            def _print(m, c):
                if c == '🔒':
                    color = Fore.RED
                elif c == '🔑':
                    color = Fore.YELLOW
                else:
                    color = Fore.GREEN

                for row in m:
                    row = [color + char + Style.RESET_ALL if char == '#' else char for char in row]
                    print(''.join(row))

                print(f"{3 * '-'}{c}{3 * '-'}")

            os.system('clear')
            _print(lock, '🔒')
            _print(key, '🔑')
            print(f"Total match: {fit}")
            if match:
                time.sleep(0.1)
                match_matrix = [[c[0] if c[0] == '#' else c[1] for c in zip(*r)] for r in zip(lock, key)]
                os.system('clear')
                _print(match_matrix, '🔐')
                print(f"Total match: {fit}")
                time.sleep(1)
            time.sleep(0.01)
            
        fit = 0
        for i, lock_height in enumerate(locks_heights):
            for j, key_height in enumerate(keys_heights):
                match = False
                try_fit = [a + b for a, b in zip(lock_height, key_height)]
                if all(t < 6 for t in try_fit):
                    fit += 1
                    match = True
                visulisation(locks[i], keys[j], match)
        
        print(f"The number of unique lock/key pairs that fit together without overlapping in any column is {fit}")


                


        
        
       