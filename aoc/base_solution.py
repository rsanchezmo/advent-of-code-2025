from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any
import time


class BaseSolution(ABC):
    """Base class for Advent of Code solutions."""

    def __init__(self, day: int, year: int = 2025):
        self.day = day
        self.year = year
        self._input: str | None = None
        self._parsed_input: Any = None

    @property
    def input_path(self) -> Path:
        """Path to the input file for this day."""
        # Go up one level from aoc/ to project root, then into dayXX/
        return Path(__file__).parent.parent / f"day{self.day:02d}" / "input.txt"

    @property
    def raw_input(self) -> str:
        """Raw input string from the input file."""
        if self._input is None:
            self._input = self.input_path.read_text().strip()
        return self._input

    def parse_input(self, raw_input: str) -> Any:
        """
        Parse the raw input string into a usable format.
        Override this method to customize parsing for each day.
        Default implementation returns lines as a list of strings.
        
        This is used when both parts share the same parsing logic.
        If parts need different parsing, override parse_input_part1/part2 instead.
        """
        return raw_input.splitlines()

    def parse_input_part1(self, raw_input: str) -> Any:
        """Parse input specifically for part 1. Override if part 1 needs different parsing."""
        return self.parse_input(raw_input)

    def parse_input_part2(self, raw_input: str) -> Any:
        """Parse input specifically for part 2. Override if part 2 needs different parsing."""
        return self.parse_input(raw_input)

    @abstractmethod
    def part1(self, input_data: Any) -> Any:
        """Solve part 1 of the puzzle."""
        pass

    @abstractmethod
    def part2(self, input_data: Any) -> Any:
        """Solve part 2 of the puzzle."""
        pass

    def solve(self, show_time: bool = True) -> tuple[Any, Any]:
        """Run both parts of the solution."""
        print(f"🎄 Advent of Code {self.year} - Day {self.day}")
        print("=" * 40)

        # Part 1
        input_data1 = self.parse_input_part1(self.raw_input)
        start = time.perf_counter()
        result1 = self.part1(input_data1)
        time1 = time.perf_counter() - start
        print(f"Part 1: {result1}")
        if show_time:
            print(f"  Time: {time1*1000:.2f}ms")

        # Part 2
        input_data2 = self.parse_input_part2(self.raw_input)
        start = time.perf_counter()
        result2 = self.part2(input_data2)
        time2 = time.perf_counter() - start
        print(f"Part 2: {result2}")
        if show_time:
            print(f"  Time: {time2*1000:.2f}ms")

        print("=" * 40)
        if show_time:
            print(f"Total time: {(time1+time2)*1000:.2f}ms")

        return result1, result2

    def test(self, test_input: str, expected1: Any = None, expected2: Any = None, 
             test_input_part2: str | None = None) -> bool:
        """
        Test the solution with sample input.
        
        Args:
            test_input: Sample input for testing (used for both parts by default)
            expected1: Expected result for part 1
            expected2: Expected result for part 2
            test_input_part2: Optional separate input for part 2 (if different from part 1)
        """
        print(f"🧪 Testing Day {self.day}")
        print("-" * 40)

        passed = True

        if expected1 is not None:
            input_data = self.parse_input_part1(test_input.strip())
            result1 = self.part1(input_data)
            status = "✅" if result1 == expected1 else "❌"
            print(f"{status} Part 1: {result1} (expected: {expected1})")
            passed = passed and (result1 == expected1)

        if expected2 is not None:
            input_for_part2 = test_input_part2 if test_input_part2 is not None else test_input
            input_data = self.parse_input_part2(input_for_part2.strip())
            result2 = self.part2(input_data)
            status = "✅" if result2 == expected2 else "❌"
            print(f"{status} Part 2: {result2} (expected: {expected2})")
            passed = passed and (result2 == expected2)

        print("-" * 40)
        return passed
