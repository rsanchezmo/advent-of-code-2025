"""Advent of Code 2025 - Day 2"""
from aoc.base_solution import BaseSolution


class Day03(BaseSolution):
    def __init__(self):
        super().__init__(day=3)

    def parse_input(self, raw_input: str):
        return raw_input.splitlines()


    def part1(self, input_data) -> int:
        
        total_joltage = 0
        for bank in input_data:
            max_first_value = max(bank[:-1])
            max_first_index = bank.index(max_first_value)
            second_max_value = max(bank[max_first_index + 1:])
            joltage = int(max_first_value) * 10 + int(second_max_value)
            total_joltage += joltage

        return total_joltage
    

    def find_sequence(self, bank: str, start: int, end: int) -> str:
        max_value = max(bank[start:end])
        max_index = bank.index(max_value, start, end)

        if end >= len(bank):
            return max_value
        return max_value + self.find_sequence(bank, max_index + 1, end + 1)

    def part2(self, input_data) -> int:
        total_joltage = 0
        for bank in input_data:
            joltage = sum(int(digit) * 10 ** (11 - idx) for idx, digit in enumerate(self.find_sequence(bank, 0, len(bank) - 11)))

            total_joltage += joltage

        return total_joltage


if __name__ == "__main__":
    solution = Day03()
    test_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
    solution.test(test_input, expected1=357, expected2=3121910778619)
    solution.solve()
