# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:07:46 2020

@author: saadk
"""
import sys
import numpy as np
import time

MAX_RUNTIME= 30000
start_time = time.process_time_ns() / pow(10, 6)
elapsed_time = 0

backtrackCount = 0

def parseGrids():
    sudokuGrids=[]

    with open('difficulty51.txt') as f:
        puzzles = f.readlines()
        for puzzle in puzzles:
            grid = np.asarray(list(puzzle))[:-1]
            grid = np.char.replace(grid, '.', '0')
            grid = grid.astype(int)
            grid9x9 = np.reshape(grid, [9,9])
            sudokuGrids.append(grid9x9.tolist())
    
    return sudokuGrids

def solve(grid): 
    getZero = check_zero(grid) #Checking for zeroes

    if not getZero:
        return True
    else:
        row, col = getZero #Found an index

    global elapsed_time
    global start_time
    currTime = time.process_time_ns()/pow(10, 6) - start_time
    elapsed_time = int(currTime)   
    if elapsed_time > MAX_RUNTIME:
        return False
    
    for i in range(1, 9+1):

        if isValid(grid, i, (row, col)):
            
            grid[row][col] = i  #if valid, replace zero.

            if solve(grid): #recursively solve it.
                return True
            
            global backtrackCount
            backtrackCount += 1
            grid[row][col] = 0 #Reset value, sorta backtrack.

    return False


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

    #Locating the sub-grid (0,1,2)
    grid_x_x = pos[1] // 3 
    grid_x_y = pos[0] // 3

    #Iterating over the actual sub-grid:
    for i in range(grid_x_y * 3, grid_x_y * 3 + 3): 
        for j in range(grid_x_x * 3, grid_x_x * 3 + 3):
            if (grid[i][j] == num) and ((i,j) != pos):
                return False

    return True


def check_zero(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 0):
                return (i, j)  

    return None 

    
def main():
    grids = parseGrids()
    print(len(grids))
    solvedCount = 0
    unsolvedCount = 0
    
    for i in range(len(grids)):
        global start_time 
        global elapsed_time 
        global backtrackCount
        start_time = time.process_time_ns()/pow(10, 6)
        elapsed_time = 0
        #start_time = time.process_time()
        backtrackCount = 0
        solvedBool = solve(grids[i])

        #end_time = time.process_time()
        #print(end_time - start_time)
        if (solvedBool):
            print("solved! - " + str(elapsed_time / 1000) + " ms" + " - Backtrack Count: " + str(backtrackCount))
            solvedCount += 1
        else:
            print("couldn't solve - " + str(elapsed_time / 1000) + " ms" + " - Backtrack Count: " + str(backtrackCount))
            unsolvedCount += 1

    
    print("Solved: " + str(solvedCount))
    print("Unsolved: " + str(unsolvedCount))

            
if __name__ == '__main__':
    main()
    

