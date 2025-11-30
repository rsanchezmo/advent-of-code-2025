"""Advent of Code 2025 - Day 1"""
from base_solution import BaseSolution


class Day01(BaseSolution):
    def __init__(self):
        super().__init__(day=1)

    def parse_input(self, raw_input: str) -> list[int]:
        """
        Parse input as a list of integers.
        Override parse_input_part1 or parse_input_part2 if parts need different parsing.
        """
        return [int(line) for line in raw_input.splitlines()]

    # Uncomment if part 2 needs different parsing:
    # def parse_input_part2(self, raw_input: str) -> dict:
    #     """Parse input differently for part 2."""
    #     lines = raw_input.splitlines()
    #     return {"values": [int(line) for line in lines], "count": len(lines)}

    def part1(self, input_data: list[int]) -> int:
        """Solve part 1."""
        # TODO: Implement part 1
        return 0

    def part2(self, input_data: list[int]) -> int:
        """Solve part 2."""
        # TODO: Implement part 2
        return 0


if __name__ == "__main__":
    solution = Day01()

    # Test with sample input
    # test_input = """
    # 1
    # 2
    # 3
    # """
    # solution.test(test_input, expected1=6, expected2=None)
    
    # If part 2 has different sample input:
    # solution.test(test_input, expected1=6, expected2=10, test_input_part2="different\ninput")

    # Solve with real input
    solution.solve()
