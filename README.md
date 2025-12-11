# 🎄 Advent of Code 2025

This repository contains my solutions for [Advent of Code 2025](https://adventofcode.com/2025) in Python.

## Project Structure

Each day's solution is structured in its own directory (e.g., `day01`, `day02`, etc.) containing:
- `solution.py`: The main solution file with `part1` and `part2` methods.
- `input.txt`: The input data for the day's challenge.

## Creating a New Day

Use the `create_day.sh` script to quickly scaffold a new day's solution:

```bash
./create_day.sh <day_number>
```

For example, `./create_day.sh 5` will create `day05/` with:
- A `solution.py` template that extends `BaseSolution`
- An empty `input.txt` file ready for your puzzle input

## Base Solution Class

All solutions extend the `BaseSolution` class from `aoc/base_solution.py`, which provides:

### Key Methods

| Method | Description |
|--------|-------------|
| `parse_input(raw_input)` | Parse raw input into a usable format (default: split by lines) |
| `parse_input_part1(raw_input)` | Custom parsing for part 1 (if different from part 2) |
| `parse_input_part2(raw_input)` | Custom parsing for part 2 (if different from part 1) |
| `part1(input_data, **kwargs)` | **Abstract** - Implement your part 1 solution |
| `part2(input_data, **kwargs)` | **Abstract** - Implement your part 2 solution |
| `solve(part1_kwargs, part2_kwargs)` | Run both parts with timing information |
| `test(test_input, expected1, expected2, test_input_part2, part1_kwargs, part2_kwargs)` | Test with sample input before solving |

### Usage Example

```python
from aoc.base_solution import BaseSolution

class Day05(BaseSolution):
    def __init__(self):
        super().__init__(day=5)

    def parse_input(self, raw_input: str):
        return raw_input.splitlines()

    def part1(self, input_data, **kwargs) -> int:
        # Your solution here
        return 0

    def part2(self, input_data, **kwargs) -> int:
        # Your solution here
        return 0

if __name__ == "__main__":
    solution = Day05()
    
    # Test with sample input
    test_input = """sample input here"""
    solution.test(test_input, expected1=123, expected2=456)
    
    # Solve with real input
    solution.solve()
```

### Using kwargs for Different Parameters

When test and solve require different parameters (e.g., grid size, iterations):

```python
def part1(self, input_data, grid_size=100, **kwargs) -> int:
    # Use grid_size parameter
    ...

if __name__ == "__main__":
    solution = Day05()
    
    # Test with smaller grid
    solution.test(test_input, expected1=12, part1_kwargs={"grid_size": 10})
    
    # Solve with full grid
    solution.solve(part1_kwargs={"grid_size": 100})
```

### Example Output

```
🧪 Testing Day 4
----------------------------------------
✅ Part 1: 13 (expected: 13)
✅ Part 2: 43 (expected: 43)
----------------------------------------
🎄 Advent of Code 2025 - Day 4
========================================
Part 1: 1523
  Time: 8.43ms
Part 2: 9290
  Time: 212.99ms
========================================
Total time: 221.42ms
```

## Progress

- [x] Day 1
- [x] Day 2
- [x] Day 3
- [x] Day 4
- [x] Day 5
- [x] Day 6
- [x] Day 7
- [x] Day 8
- [x] Day 9
- [x] Day 10
- [x] Day 11
- [ ] Day 12
