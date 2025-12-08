"""Advent of Code 2025 - Day 8"""
from aoc.base_solution import BaseSolution


class Day08(BaseSolution):
    def __init__(self):
        super().__init__(day=8)

    def parse_input(self, raw_input: str):
        return {tuple(map(int, line.split(','))) for line in raw_input.splitlines()}

    @staticmethod
    def _euclidean_distance(a, b) -> float:
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5
    
    @staticmethod
    def _get_sorted_distances(points):
        distance_map = {} # point_a, pointb -> distance
        for point_a in points:
            for point_b in points:
                if point_a == point_b or (min(point_a, point_b), max(point_a, point_b)) in distance_map:
                    continue
                distance = Day08._euclidean_distance(point_a, point_b)
                distance_map[(min(point_a, point_b), max(point_a, point_b))] = distance

        sorted_distances = sorted(distance_map.items(), key=lambda x: x[1])
        return sorted_distances


    def part1(self, input_data, iterations=10, **kwargs) -> int:
        points = input_data
        sorted_distances = Day08._get_sorted_distances(points)

        circuits = []
        n_pairs_processed = 0
        for (point_a, point_b), _ in sorted_distances:
            if n_pairs_processed >= iterations:
                break
            n_pairs_processed += 1

            circuit_a = None
            circuit_b = None
            for circuit in circuits:
                if point_a in circuit:
                    circuit_a = circuit
                if point_b in circuit:
                    circuit_b = circuit
                if circuit_a and circuit_b:
                    break
            
            if circuit_a and circuit_b:
                if circuit_a != circuit_b:
                    circuit_a.update(circuit_b)
                    circuits.remove(circuit_b)
                else:
                    continue
            elif circuit_a:
                circuit_a.add(point_b)
            elif circuit_b:
                circuit_b.add(point_a)
            else:
                circuits.append({point_a, point_b})

        # sort circuits by size in descending order
        circuits.sort(key=lambda x: len(x), reverse=True)
        first_len, second_len, third_len = len(circuits[0]), len(circuits[1]), len(circuits[2])
        return first_len * second_len * third_len


    def part2(self, input_data, **kwargs) -> int:
        points = input_data
        sorted_distances = Day08._get_sorted_distances(points)

        circuits = []
        for (point_a, point_b), _ in sorted_distances:
            circuit_a = None
            circuit_b = None
            for circuit in circuits:
                if point_a in circuit:
                    circuit_a = circuit
                if point_b in circuit:
                    circuit_b = circuit
                if circuit_a and circuit_b:
                    break
            
            if circuit_a and circuit_b:
                if circuit_a != circuit_b:
                    circuit_a.update(circuit_b)
                    circuits.remove(circuit_b)
                else:
                    continue
            elif circuit_a:
                circuit_a.add(point_b)
            elif circuit_b:
                circuit_b.add(point_a)
            else:
                circuits.append({point_a, point_b})

            if len(circuits[0]) == len(points):
                return point_a[0] * point_b[0]
            
        return 0


if __name__ == "__main__":
    solution = Day08()

    test_input = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
    solution.test(test_input, expected1=40, expected2=25272, part1_kwargs={"iterations": 10})
    solution.solve(part1_kwargs={"iterations": 1000})
