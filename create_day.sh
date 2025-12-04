#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./create_day.sh <day_number>"
    exit 1
fi

DAY_NUM=$1
DAY_PADDED=$(printf "%02d" $DAY_NUM)
DAY_DIR="day${DAY_PADDED}"

if [ -d "$DAY_DIR" ]; then
    echo "Error: $DAY_DIR already exists!"
    exit 1
fi

mkdir -p "$DAY_DIR"
touch "$DAY_DIR/input.txt"

cat > "$DAY_DIR/solution.py" << EOF
"""Advent of Code 2025 - Day ${DAY_NUM}"""
from aoc.base_solution import BaseSolution


class Day${DAY_PADDED}(BaseSolution):
    def __init__(self):
        super().__init__(day=${DAY_NUM})

    def parse_input(self, raw_input: str):
        return raw_input.splitlines()

    def part1(self, input_data) -> int:
        # TODO: implement
        return 0

    def part2(self, input_data) -> int:
        # TODO: implement
        return 0


if __name__ == "__main__":
    solution = Day${DAY_PADDED}()

    test_input = """
"""
    solution.test(test_input, expected1=None, expected2=None)
    solution.solve()
EOF

echo "Created $DAY_DIR/ with solution.py and input.txt"
