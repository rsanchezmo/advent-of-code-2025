"""Advent of Code 2025 - Day 8"""
from aoc.base_solution import BaseSolution


class Day08(BaseSolution):
    def __init__(self):
        super().__init__(day=8)

    def parse_input(self, raw_input: str):
        return raw_input.splitlines()

    def part1(self, input_data) -> int:
        # TODO: implement
        return 0

    def part2(self, input_data) -> int:
        # TODO: implement
        return 0


if __name__ == "__main__":
    solution = Day08()

    test_input = """
"""
    solution.test(test_input, expected1=None, expected2=None)
    solution.solve()
