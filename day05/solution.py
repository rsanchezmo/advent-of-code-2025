"""Advent of Code 2025 - Day 5"""
from aoc.base_solution import BaseSolution


class Day05(BaseSolution):
    def __init__(self):
        super().__init__(day=5)

    def parse_input(self, raw_input: str):
        range_lines, number_lines = raw_input.strip().split("\n\n")
        ranges = []
        for line in range_lines.splitlines():
            start, end = map(int, line.split("-"))
            ranges.append((start, end))

        numbers = [int(line) for line in number_lines.splitlines()]
        return ranges, numbers

    def part1(self, input_data) -> int:
        ranges, numbers = input_data
        merged_ranges = Day05.merge_ranges(ranges)
        fresh_numbers = 0
        
        for number in numbers:
            for start, end in merged_ranges:
                if start <= number <= end:
                    fresh_numbers += 1
                    break
        return fresh_numbers

    @staticmethod
    def merge_ranges(ranges):
        merged_ranges = []
        for start, end in sorted(ranges):
            if not merged_ranges or merged_ranges[-1][1] < start - 1:
                # if the end is after the last end in merged_ranges, add a new range
                merged_ranges.append([start, end])
            else:
                # if the starting value is between the last range, update the end if needed
                merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
        return merged_ranges

    def part2(self, input_data) -> int:
        ranges, _ = input_data

        merged_ranges = Day05.merge_ranges(ranges)
        fresh_numbers = sum(end - start + 1 for start, end in merged_ranges)
        return fresh_numbers


if __name__ == "__main__":
    solution = Day05()

    test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
    solution.test(test_input, expected1=3, expected2=14)
    solution.solve()
