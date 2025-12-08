"""Advent of Code 2025 - Day 1"""
from aoc.base_solution import BaseSolution


class Day01(BaseSolution):
    def __init__(self):
        super().__init__(day=1)

    def parse_input(self, raw_input: str):
        def _parse_orientation(s: str):
            return -1 if s == 'L' else 1
        return [(_parse_orientation(line[0]), int(line[1:].strip())) for line in raw_input.splitlines()]


    def part1(self, input_data, **kwargs) -> int:
        dial = 50

        counts_0 = 0
        for turn, steps in input_data:
            dial = (dial + turn * steps) % 100
            counts_0 += (dial == 0)

        return counts_0

    def part2(self, input_data, **kwargs) -> int:
        dial = 50

        counts_0 = 0
        for turn, steps in input_data:
            div, mod = divmod(turn * steps + dial, 100)

            # Count how many times we pass through 0 during this move
            n_counts = abs(div) - (dial == 0 and turn == -1) + (mod == 0 and turn == -1)
            dial = mod
            counts_0 += n_counts

        return counts_0


if __name__ == "__main__":
    solution = Day01()

    test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
    solution.test(test_input, expected1=3, expected2=6)
    solution.solve()
