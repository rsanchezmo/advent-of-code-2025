"""Advent of Code 2025 - Day 9"""
from aoc.base_solution import BaseSolution
from itertools import combinations
from collections import defaultdict
from shapely import Polygon

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
    
    @staticmethod
    def get_boundary_points(input_data):
        all_points = []
        
        def add_line_points(p1, p2):
            if p1[0] == p2[0]:  # vertical line
                for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    all_points.append((p1[0], y))
            elif p1[1] == p2[1]:  # horizontal line
                for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                    all_points.append((x, p1[1]))
        
        for i in range(len(input_data)):
            add_line_points(input_data[i], input_data[(i + 1) % len(input_data)])
        
        return all_points


    # SLOW VERSION
    def part2(self, input_data, **kwargs) -> int:
        boundary_points = set(Day09.get_boundary_points(input_data))
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        for x, y in boundary_points:
            rows[y].append(x)
            cols[x].append(y)
        
        # Sort to easily access min (left/top) and max (right/bottom) bounds
        for r in rows.values(): r.sort()
        for c in cols.values(): c.sort()

        max_area = 0
        for p1, p2 in combinations(input_data, 2):
            area = Day09._get_area(p1, p2)
            if area <= max_area:
                continue

            # Determine intersection points of the rectangle
            i1 = (p1[0], p2[1])
            i2 = (p2[0], p1[1])

            is_valid = True
            polygon_points = Day09.get_boundary_points([p1, i1, p2, i2])
            for ix, iy in polygon_points:
                # If it's part of the boundary, it's valid immediately
                if (ix, iy) in boundary_points:
                    continue
            
                # raycasting checks
                # Check Horizontal (Left/Right)
                if iy not in rows or not (rows[iy][0] < ix < rows[iy][-1]):
                    is_valid = False
                    break
                
                # Check Vertical (Up/Down)
                if ix not in cols or not (cols[ix][0] < iy < cols[ix][-1]):
                    is_valid = False
                    break
            
            if is_valid:
                max_area = area

        return max_area
    
    # FAST VERSION
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
