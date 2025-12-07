"""Advent of Code 2025 - Day 6"""
from aoc.base_solution import BaseSolution


class Day06(BaseSolution):
    def __init__(self):
        super().__init__(day=6)

    def parse_input(self, raw_input: str):
        lines = raw_input.strip().splitlines()
        numbers = []
        for line in lines[:-1]:
            row = [int(x) for x in line.split() if x]
            numbers.append(row)
        operands = [x for x in lines[-1].split() if x]
        numbers = list(zip(*numbers))
        return numbers, operands
    
    def parse_input_part2(self, raw_input: str):
        lines = raw_input.strip().splitlines()
        
        # find operand positions in the last line
        operand_cols = [(idx, char) for idx, char in enumerate(lines[-1]) if char in "+*"]
        operands = [op for _, op in operand_cols]

        # find column size and then extract numbers vertically
        numbers = []
        for i in range(len(operand_cols)):
            group_nums = []
            start_idx = operand_cols[i][0]
            end_idx = operand_cols[i + 1][0] if i + 1 < len(operand_cols) else len(lines[0])
            group_nums = []
            for col in range(start_idx, end_idx):
                col_num = ''.join(line[col] for line in lines[:-1]).strip()
                if col_num:
                    group_nums.append(int(col_num))
            numbers.append(group_nums)
        return numbers, operands
    
    @staticmethod
    def _calc(numbers: list[int], operand: str):
        if operand == "+":
            return sum(numbers)
        elif operand == "*":
            prod = 1
            for n in numbers:
                prod *= n
            return prod
        return 0

    def part1(self, input_data) -> int:
        result = 0
        for numbers, operand in zip(*input_data):
            result += self._calc(numbers, operand)
        return result

    def part2(self, input_data) -> int:
        return self.part1(input_data)


if __name__ == "__main__":
    solution = Day06()

    test_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""
    solution.test(test_input, expected1=4277556, expected2=3263827)
    solution.solve()
