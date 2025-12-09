"""Advent of Code 2025 - Day 9"""
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
    
    def part2(self, input_data, **kwargs) -> int:
        boundary_points = Day09.get_boundary_points(input_data)
        boundary_points = set(boundary_points)

        max_area = 0
        for start_point_idx in range(len(input_data)):
            for end_point_idx in range(start_point_idx + 1, len(input_data)):
                start_point = input_data[start_point_idx]
                end_point = input_data[end_point_idx]
                
                area = Day09._get_area(start_point, end_point)
                if area > max_area:

                    # apply raycasting on each rectangle intersection point, each intersection point must have at least 1 boundary point at each direction
                    is_valid = True
                    for intersection_point in (
                        (start_point[0], end_point[1]),
                        (end_point[0], start_point[1])
                    ):
                        if intersection_point in boundary_points:
                            continue
                        
                        # count boundary points on each direction (stop early with any())
                        left_count = any(p[1] == intersection_point[1] and p[0] < intersection_point[0] for p in boundary_points)
                        right_count = any(p[1] == intersection_point[1] and p[0] > intersection_point[0] for p in boundary_points)
                        up_count = any(p[0] == intersection_point[0] and p[1] < intersection_point[1] for p in boundary_points)
                        down_count = any(p[0] == intersection_point[0] and p[1] > intersection_point[1] for p in boundary_points)

                        if not (right_count and left_count and up_count and down_count):
                            is_valid = False
                            break
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
