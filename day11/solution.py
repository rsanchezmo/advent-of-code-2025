"""Advent of Code 2025 - Day 11"""
from aoc.base_solution import BaseSolution
from functools import cache


class Day11(BaseSolution):
    def __init__(self):
        super().__init__(day=11)

    def parse_input(self, raw_input: str):
        graph = {}
        for line in raw_input.strip().splitlines():
            node, connected_nodes_str = line.split(":")
            connected_nodes = connected_nodes_str.strip().split() if connected_nodes_str.strip() else []
            graph[node.strip()] = set(connected_nodes)
        return graph

    def part1(self, input_data, **kwargs) -> int:
        graph = input_data
        start_node = "you"
        target_node = "out"

        @cache
        def solve_with_requirements(node):
            if node == target_node:
                return 1

            total_paths = 0
            for neighbor in graph.get(node, []):
                total_paths += solve_with_requirements(neighbor)
            
            return total_paths

        return solve_with_requirements(start_node)
    
    def part2(self, input_data, **kwargs) -> int:
        graph = input_data
        start_node = "svr"
        target_node = "out"
        initial_required = frozenset({"fft", "dac"})

        @cache
        def solve_with_requirements(node, required):
            if node in required:
                required = required - {node}
            
            if node == target_node:
                # Only count path if all required nodes have been visited
                return 1 if not required else 0

            total_paths = 0
            for neighbor in graph.get(node, []):
                total_paths += solve_with_requirements(neighbor, required)
            
            return total_paths

        return solve_with_requirements(start_node, initial_required)


if __name__ == "__main__":
    solution = Day11()

    test_input = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

    test_iput_2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
    solution.test(test_input, expected1=5, expected2=2, test_input_part2=test_iput_2)
    solution.solve()
