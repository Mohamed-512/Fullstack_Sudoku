# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:07:46 2020

Algorithm to solve 9x9 Sudoku Grid.

@author: saadk
"""
import sys
import json
import random
import numpy as np

'''
JSON Object Form:
{
	"grid": {
		"initialGrid":
    	[
            [
				0, 5, 0, 6, 3, 2, 9, 4, 1
            ],
            [
				0, 0, 4, 0, 0, 0, 3, 0, 0
            ],
            [
				9, 2, 3, 0, 0, 0, 0, 0, 8
            ],
            [
				0, 9, 0, 3, 2, 4, 0, 0, 0
            ],
            [
            	0, 0, 5, 0, 0, 0, 8, 0, 0
            ],
            [
            	0, 0, 0, 8, 5, 6, 0, 9, 0
            ],
            [
            	3, 0, 0, 0, 0, 0, 6, 8, 9
            ],
            [
            	0, 0, 6, 0, 0, 0, 4, 0, 0
            ],
            [
            	4, 8, 9, 2, 6, 1, 0, 7, 0
            ]
        ],
        "attemptGrid":
        [
            [
				4, 5, 8, 6, 3, 2, 9, 4, 1
            ],
            [
				6, 0, 4, 0, 0, 0, 3, 0, 0
            ],
            [
				9, 2, 3, 0, 0, 0, 0, 0, 8
            ],
            [
				0, 9, 0, 3, 2, 4, 0, 0, 0
            ],
            [
            	0, 0, 5, 0, 0, 0, 8, 0, 0
            ],
            [
            	0, 0, 0, 8, 5, 6, 0, 9, 0
            ],
            [
            	3, 0, 0, 0, 0, 0, 6, 8, 9
            ],
            [
            	0, 0, 6, 0, 0, 0, 4, 0, 0
            ],
            [
            	4, 8, 9, 2, 6, 1, 0, 7, 0
            ]
        ]
	}

}
'''


def main():
    if (len(sys.argv) == 3):
        # Checking solution & possibility for gird to be solved
        gridToSolve = json.loads(sys.argv[1])
        gridAttempt = json.loads(sys.argv[2])
        print('{"Solvable_Grid?":'+str(solve(gridToSolve)).lower() +
              ', "Solution_Correct?":'+str(checkSolution(gridToSolve, gridAttempt)).lower()+"}")
    elif (len(sys.argv) == 2):
        # Trying to solve grid
        gridToSolve = json.loads(sys.argv[1])
        couldSolve = solve(gridToSolve)
        solvedGrid = {"solvedGrid": gridToSolve, "couldSolve": couldSolve}
        print(json.dumps(solvedGrid))
    elif (len(sys.argv) == 1):
        # Generating a random initial grid
        initialGrid = buildGrid()
        initialGrid = {"initialGrid": initialGrid}
        print(json.dumps(initialGrid))

    sys.stdout.flush()


def checkSolution(gridToSolve, gridAttempt):
    flattenedSolvedGrid = [j for sub in gridToSolve for j in sub]
    flattenedAttemptGrid = [j for sub in gridAttempt for j in sub]

    # The assumption here is that the sudoku grid has ONE unique solution.
    # which is consistent with a valid sudoku grid.

    if (len(flattenedSolvedGrid) == len(flattenedAttemptGrid)):
        for i in range(len(flattenedSolvedGrid)):
            if (flattenedSolvedGrid[i] != flattenedAttemptGrid[i]) or flattenedAttemptGrid[i] == 0:
                return False
    return True


def solve(grid):
    getZero = check_zero(grid)  # Checking for zeroes

    if not getZero:
        return True
    else:
        row, col = getZero  # Found an index

    for i in range(1, 9+1):

        if isValid(grid, i, (row, col)):

            grid[row][col] = i  # if valid, replace zero.

            if solve(grid):  # recursively solve it.
                return True

            grid[row][col] = 0  # Reset value, sorta backtrack.

    return False


def buildGrid():
    initialGrid = np.zeros((9, 9))
    covered_cells = {}

    while len(covered_cells) < 34:
        rand_column = random.randint(0, 8)
        rand_row = random.randint(0, 8)
        rand_num = random.randint(1, 9)

        if (rand_row, rand_column) not in covered_cells and isValid(initialGrid, rand_num, (rand_row, rand_column)):
            covered_cells.update({(rand_row, rand_column): rand_num})
            initialGrid[rand_row, rand_column] = rand_num
        else:
            continue

        if not solve(initialGrid.tolist()):
            # Backtracking if the new number make it not solvable
            del covered_cells[(rand_row, rand_column)]
            initialGrid[rand_row, rand_column] = 0

    return initialGrid.tolist()


def isValid(grid, num, pos):

    # Scanning the columns
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Scanning the rows
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Scanning 3x3 sub-grid for possibilities

    # Locating the sub-grid (0,1,2)
    grid_x_x = pos[1] // 3
    grid_x_y = pos[0] // 3

    # Iterating over the actual sub-grid:
    for i in range(grid_x_y * 3, grid_x_y * 3 + 3):
        for j in range(grid_x_x * 3, grid_x_x * 3 + 3):
            if (grid[i][j] == num) and ((i, j) != pos):
                return False

    return True


def check_zero(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 0):
                return (i, j)

    return None


if __name__ == '__main__':
    main()
