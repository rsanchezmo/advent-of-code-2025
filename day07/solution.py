"""Advent of Code 2025 - Day 7"""
from aoc.base_solution import BaseSolution


class Day07(BaseSolution):

    def __init__(self):
        super().__init__(day=7)

    def parse_input(self, raw_input: str):
        data = raw_input.splitlines()
        starting_loc = (0, data[0].index('S'))
        return starting_loc, data

    def part1(self, input_data) -> int:
        starting_loc, diagram = input_data

        queue = {starting_loc}
        splitters = set()
        while queue:
            row, col = queue.pop()
            down_pos = (row + 1, col)

            if row >= len(diagram) - 1:
                continue

            if diagram[down_pos[0]][down_pos[1]] == '^':
                splitters.add(down_pos)
                if col - 1 >= 0:
                    queue.add((row + 1, col - 1))
                if col + 1 < len(diagram[0]):
                    queue.add((row + 1, col + 1))
            else:
                queue.add(down_pos)

        return len(splitters)
            
    def part2(self, input_data) -> int:
        starting_loc, diagram = input_data
        diagram_result = [[0] * len(diagram[0]) for _ in range(len(diagram))]
        diagram_result[starting_loc[0]][starting_loc[1]] = 1

        queue = [starting_loc]
        visited = set()
        while queue:
            row, col = queue.pop(0)

            if (row, col) in visited:
                continue
            visited.add((row, col))

            current_count = diagram_result[row][col]

            if row >= len(diagram) - 1:
                continue

            if diagram[row + 1][col] == '^':
                for new_row, new_col in ((row + 1, col - 1), (row + 1, col + 1)):
                    if 0 <= new_col <= len(diagram[0]):
                        queue.append((new_row, new_col)) 
                        diagram_result[new_row][new_col] += current_count
            else:
                new_row, new_col = row + 1, col
                queue.append((new_row, new_col))
                diagram_result[new_row][new_col] += current_count


        return sum(diagram_result[-1]) # all the paths are propagated till this row



if __name__ == "__main__":
    solution = Day07()

    test_input = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
    solution.test(test_input, expected1=21, expected2=40)
    solution.solve()
