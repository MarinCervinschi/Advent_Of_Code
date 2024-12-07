
class Backtracking:
    def __init__(self, _dict):
        self._dict = _dict
        self.good_answers = set()

    def find(self, nums, target, part_2):

        def rec(index, current_result):
            if index == len(nums):
                if current_result == target:
                    self.good_answers.add(target)
                return

            next_num = nums[index]

            rec(index + 1, current_result + next_num)

            rec(index + 1, current_result * next_num)

            if part_2:
                rec(index + 1, int(str(current_result) + str(next_num)))

        rec(1, nums[0])

    def part_1(self):
        for result, nums in self._dict.items():
            self.find(nums, int(result), part_2=False)
        return sum(self.good_answers)

    def part_2(self):
        for result, nums in self._dict.items():
            self.find(nums, int(result), part_2=True)
        return sum(self.good_answers)