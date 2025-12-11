"""Advent of Code 2025 - Day 9"""

from itertools import combinations

from shapely import Polygon

from aoc.base_solution import BaseSolution


class Day09(BaseSolution):
    def __init__(self):
        super().__init__(day=9)

    def parse_input(self, raw_input: str):
        return [tuple(map(int, line.split(","))) for line in raw_input.splitlines()]

    @staticmethod
    def _get_area(start_point, end_point) -> int:
        return (1 + abs(end_point[0] - start_point[0])) * (1 + abs(end_point[1] - start_point[1]))

    def part1(self, input_data, **kwargs) -> int:
        max_area = 0
        for start_point_idx in range(len(input_data)):
            for end_point_idx in range(start_point_idx + 1, len(input_data)):
                start_point = input_data[start_point_idx]
                end_point = input_data[end_point_idx]
                area = Day09._get_area(start_point, end_point)
                if area > max_area:
                    max_area = area

        return max_area

    def part2(self, input_data, **kwargs) -> int:
        boundary_polygon = Polygon(input_data)

        max_area = 0
        for p1, p2 in combinations(input_data, 2):
            area = Day09._get_area(p1, p2)
            if area <= max_area:
                continue

            # Determine intersection points of the rectangle
            i1 = (p1[0], p2[1])
            i2 = (p2[0], p1[1])

            is_valid = True
            rectangle = Polygon([p1, i1, p2, i2])
            # check if the polygon is inside the boundary polygon
            if not rectangle.within(boundary_polygon):
                is_valid = False

            if is_valid:
                max_area = area
        return max_area


if __name__ == "__main__":
    solution = Day09()

    test_input = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
    solution.test(test_input, expected1=50, expected2=24)
    solution.solve()
