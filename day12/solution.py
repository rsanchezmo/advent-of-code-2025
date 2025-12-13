"""Advent of Code 2025 - Day 12"""
from aoc.base_solution import BaseSolution


class Day12(BaseSolution):
    def __init__(self):
        super().__init__(day=12)

    def parse_input(self, raw_input: str):
        lines = raw_input.strip().split("\n")
        
        presents = {}  # id -> list of (row, col) offsets where '#' appears
        grids = []  # list of (width, height, [freq of that col of presents])
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if not line:
                i += 1
                continue
            
            if line.endswith(":") and line[:-1].isdigit():
                present_id = int(line[:-1])
                shape = []
                # Read the next 3 lines for the shape
                for row in range(3):
                    i += 1
                    shape_line = lines[i]
                    for col, char in enumerate(shape_line):
                        if char == "#":
                            shape.append((row, col))
                presents[present_id] = shape
            
            elif "x" in line and ":" in line:
                size_part, presents_part = line.split(":")
                width, height = map(int, size_part.split("x"))
                present_ids = list(map(int, presents_part.strip().split()))
                grids.append((width, height, present_ids))
            
            i += 1
        
        return presents, grids


    def part1(self, input_data, **kwargs) -> int:
        _, grids = input_data
        
        solvable_count = 0
        for width, height, present_freqs in grids:
            grid_area = width * height 

            required_area = sum(present_freqs) * 9
            if required_area <= grid_area:
                solvable_count += 1 
        
        return solvable_count


    def part2(self, input_data, **kwargs) -> int:
        # TODO: implement
        return 0


if __name__ == "__main__":
    solution = Day12()

    test_input = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""
    solution.test(test_input, expected1=2, expected2=None)
    solution.solve()
