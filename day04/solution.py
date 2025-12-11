"""Advent of Code 2025 - Day 4"""

from aoc.base_solution import BaseSolution


class Day04(BaseSolution):
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def __init__(self):
        super().__init__(day=4)

    def parse_input(self, raw_input: str):
        return {(r, c) for r, line in enumerate(raw_input.splitlines()) for c, ch in enumerate(line) if ch == "@"}

    def part1(self, input_data, **kwargs) -> int:
        return len(Day04._find_accessible_rolls(input_data))

    @staticmethod
    def _find_removable_rolls(pos, basemap):
        row, col = pos
        return sum((row + move[0], col + move[1]) in basemap for move in Day04.MOVES)

    @staticmethod
    def _find_accessible_rolls(basemap):
        return {pos for pos in basemap if Day04._find_removable_rolls(pos, basemap) < 4}

    def part2(self, input_data, **kwargs) -> int:
        basemap = input_data.copy()

        accessible_rolls = 0
        while removed_rolls := Day04._find_accessible_rolls(basemap):
            accessible_rolls += len(removed_rolls)
            basemap -= removed_rolls

        return accessible_rolls


if __name__ == "__main__":
    solution = Day04()

    test_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
    solution.test(test_input, expected1=13, expected2=43)
    solution.solve()
