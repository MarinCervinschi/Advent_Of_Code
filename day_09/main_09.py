    
class Solution:

    def __init__(self, disk_map):
        self.disk_map = self.one_block(disk_map)

    def one_block(self, disk_map):
        disk = []
        j = 0
        for i, length in enumerate(disk_map):
            if i % 2 == 0:
                disk.extend(length * [str(j)])
                j += 1
            else:
                disk.extend(length * ['.'])
        
        return disk
    
    # -------------------------- Part 1 -------------------------- #

    def rearrange_part_1(self, disk):
        j = len(disk)
        for i in range(len(disk)):
            if i >= j:
                break
            if disk[i] == '.':
                while True:
                    j -= 1
                    if disk[j] != '.':
                        break
                disk[i], disk[j] = disk[j], '.'
        return disk
    

    def part_1(self):
        rerranged = self.rearrange_part_1(self.disk_map[:])
        return sum(i * int(block) for i, block in enumerate(rerranged) if block != '.')

    # -------------------------- Part 2 -------------------------- #

    def no_block_len(self, disk, len_block, k):
        i, n = 0, len(disk)
        while i < n and i <= k:
            if disk[i] == '.':
                start_index_free_space = i
                len_no_block = 0
                while i < n and disk[i] == '.':
                    len_no_block += 1
                    i += 1
                if len_block <= len_no_block:
                    return len_no_block, start_index_free_space
                else:
                    continue
            i += 1
        return 0, 0
    
    def move(self, i, disk, len_block, start_index_free_space):
        i += len_block
        for _ in range(len_block):
            disk[i], disk[start_index_free_space] = '.', disk[i]
            i -= 1
            start_index_free_space += 1

    def rearrange_part_2(self, disk):
        i = len(disk) - 1
        while i != -1:
            block = disk[i]
            if block == '.':
                i -= 1
                continue

            len_block = 0
            while disk[i] == block:
                i -= 1
                len_block += 1

            _no_block_len, start_index_free_space = self.no_block_len(disk, len_block, i)
            if len_block <= _no_block_len:
                self.move(i, disk, len_block, start_index_free_space)
                    
        return disk
    
    def part_2(self):
        rerranged = self.rearrange_part_2(self.disk_map[:])
        return sum(i * int(block) for i, block in enumerate(rerranged) if block != '.')
    

if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = [int(c) for c in f.read()]

        sol = Solution(puzzle)
        print([sol.part_1(), sol.part_2()])
