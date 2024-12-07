
class Backtracking:

    def __init__(self, _dict):
        self._dict = _dict
        self.good_anwers = set()

    def check(self, nums, operations, result, part_2):
        j = 0
        execution = nums[0]
        for i in range(1, len(nums)):
            if operations[j] == '+':
                execution += nums[i]
            elif operations[j] == '*':
                execution *= nums[i]
            elif part_2:
                execution = int(str(execution) + str(nums[i]))

            if i != len(nums) - 1:
                j += 1

        return execution == result
    

    def rec(self, nums, operations, i, result, part_2):
        if i == len(nums) - 1:
            if self.check(nums, operations, result, part_2):
                self.good_anwers.add(result)
            return
        
        for op in ['+', '*'] + (['|'] if part_2 else []):
            self.rec(nums, operations + [op], i + 1, result, part_2)
    
    def part_1(self):
        for result, nums in self._dict.items():
            self.rec(nums, [], 0, int(result), False)
        return sum(self.good_anwers)
    
    def part_2(self):
        for result, nums in self._dict.items():
            self.rec(nums, [], 0, int(result), True)
        return sum(self.good_anwers)

