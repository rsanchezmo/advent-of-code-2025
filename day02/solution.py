"""Advent of Code 2025 - Day 2"""

import re

from aoc.base_solution import BaseSolution


class Day02(BaseSolution):
    def __init__(self):
        super().__init__(day=2)

    def parse_input(self, raw_input: str):
        return [(int(line.split("-")[0]), int(line.split("-")[1])) for line in raw_input.strip().split(",")]

    def part1(self, input_data, **kwargs) -> int:
        total_sum = 0
        for start, end in input_data:
            for n in range(start, end + 1):
                s = str(n)
                if len(s) % 2 != 0:
                    continue

                mid = len(s) // 2
                if s[:mid] == s[mid:]:
                    total_sum += n
        return total_sum

    def part2(self, input_data, **kwargs) -> int:
        pattern = re.compile(r"(.+?)\1{1,}")
        total_sum = 0

        for start, end in input_data:
            for n in range(start, end + 1):
                s = str(n)
                if pattern.fullmatch(s):
                    total_sum += n

        return total_sum


if __name__ == "__main__":
    solution = Day02()

    test_input = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""
    solution.test(test_input, expected1=1227775554, expected2=4174379265)
    solution.solve()
