"""Advent of Code 2025 - Day 10"""
from aoc.base_solution import BaseSolution
from itertools import product
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

class Day10(BaseSolution):
    def __init__(self):
        super().__init__(day=10)

    def parse_input(self, raw_input: str):
        # Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.
        lines = raw_input.strip().splitlines()
        parsed_data = []
        for line in lines:
            light_diagram = line[line.index('[')+1:line.index(']')]
            light_diagram = [int(c == '#') for c in light_diagram]
            wiring_schematics = []
            start = line.index(']') + 1
            while '(' in line[start:]:
                open_paren = line.index('(', start)
                close_paren = line.index(')', open_paren)
                schema = line[open_paren+1:close_paren]
                wiring_schematics.append(schema)
                start = close_paren + 1
            curly_start = line.index('{', start)
            curly_end = line.index('}', curly_start)
            joltage_requirements = line[curly_start+1:curly_end]
            joltage_requirements = list(map(int, joltage_requirements.split(',')))
            parsed_data.append((light_diagram, wiring_schematics, joltage_requirements))
        return parsed_data 
    

    @staticmethod
    def find_optimal_sol(light_diagram, wiring_schematics):
        # 1. Build Matrix Representation
        # Each row represents a light, each column a button
        # Entry is 1 if button affects light, else 0
        # 2. Set up system of equations Ax = b (mod 2)
        # A = matrix from step 1
        # x = button presses (0 or 1)
        # b = desired light states (from light_diagram)
        # 3. Use Gaussian elimination to solve for x, minimizing Hamming weight (number of 1s in x) 

        n_lights = len(light_diagram)
        n_buttons = len(wiring_schematics)
        matrix = [[0] * n_buttons for _ in range(n_lights)]
        
        for j, b_def in enumerate(wiring_schematics):
            indices = map(int, b_def.split(','))
            for i in indices:
                if i < n_lights:
                    matrix[i][j] = 1

        # Create augmented matrix [A | b]
        aug = [row[:] + [light_diagram[i]] for i, row in enumerate(matrix)]
        rows, cols = n_lights, n_buttons

        pivots = [] # Stores (row, col) of pivot elements
        pivot_row = 0
        
        # Forward Elimination (Row Echelon Form)
        for col in range(cols):
            if pivot_row >= rows:
                break
                
            # Find a pivot in current column (must be 1)
            if aug[pivot_row][col] == 0:
                for r in range(pivot_row + 1, rows):
                    if aug[r][col] == 1:
                        aug[pivot_row], aug[r] = aug[r], aug[pivot_row] # Swap rows
                        break
                else:
                    continue # No pivot in this column, it's a free variable
            
            # Eliminate other rows
            pivots.append((pivot_row, col))
            for r in range(rows):
                if r != pivot_row and aug[r][col] == 1:
                    # Row operation: R_r = R_r XOR R_pivot
                    for c in range(col, cols + 1):
                        aug[r][c] ^= aug[pivot_row][c]
            
            pivot_row += 1

        # 4. Back Substitution & Minimize Hamming Weight
        pivot_cols = {c for r, c in pivots}
        free_cols = [c for c in range(cols) if c not in pivot_cols]

        min_presses = 9999999999999

        # Iterate all combinations of free variables (2^k)
        # This finds the specific solution vector with minimal Hamming weight (sum of 1s)
        for free_vals in product([0, 1], repeat=len(free_cols)):
            x = [0] * cols
            
            # Set free variables
            for i, col_idx in enumerate(free_cols):
                x[col_idx] = free_vals[i]
                
            # Solve for pivot variables (back-substitution)
            # We iterate in reverse to solve from bottom-up
            for r, c in reversed(pivots):
                # x_c = constant ^ sum(known_vars)
                val = aug[r][cols]
                for k in range(c + 1, cols):
                    if aug[r][k] == 1:
                        val ^= x[k]
                x[c] = val
            # Calculate cost (Hamming weight)
            presses = sum(x)
            if presses < min_presses:
                min_presses = presses

        return min_presses

    def part1(self, input_data, **kwargs) -> int:
        button_press_count = 0
        for machine in input_data:
            light_diagram, wiring_schematics, joltage_requirements = machine
            min_presses = self.find_optimal_sol(light_diagram, wiring_schematics)
            button_press_count += min_presses
                
        return button_press_count
    
    @staticmethod
    def lp_minimize(joltage_requirements, wiring_schematics):
        # Integer Linear Programming (ILP)
        # Minimize c^T x  subject to Ax = b, x >= 0, x is integer
        
        n_counters = len(joltage_requirements)
        n_buttons = len(wiring_schematics)
        
        # Build A matrix and b vector
        A = np.zeros((n_counters, n_buttons))
        b = np.array(joltage_requirements)
        
        for j, b_def in enumerate(wiring_schematics):
            indices = map(int, b_def.split(','))
            for i in indices:
                if i < n_counters:
                    A[i, j] = 1

        c = np.ones(n_buttons) # Minimize total presses
        
        # Create Constraints for scipy.optimize.milp
        # A x = b  =>  lb <= A x <= ub  (where lb=ub=b)
        constraints = LinearConstraint(A, b, b)
        
        # Integrality constraint: 1 means integer, 0 means continuous
        integrality = np.ones(n_buttons)
        
        # Bounds: x >= 0
        bounds = Bounds(lb=0, ub=np.inf)
        
        res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
        if res.success:
            return int(round(res.fun))

        return 0

    def part2(self, input_data, **kwargs) -> int:
        total_button_presses = 0
        for machine in input_data:
            _, wiring_schematics, joltage_requirements = machine
            min_presses = self.lp_minimize(joltage_requirements, wiring_schematics)
            total_button_presses += min_presses
        return total_button_presses


if __name__ == "__main__":
    solution = Day10()

    test_input = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
    solution.test(test_input, expected1=7, expected2=33)
    solution.solve()
