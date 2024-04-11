#!/usr/bin/python3
'''
Calculates the perimeter of a grid-based island.
'''


def island_perimeter(grid):
    '''Returns the perimeter of an island.

    Args:
    grid (list): A 2D matrix representing the grid containing the island
                 whose perimeter is to be calculated.

    Returns: the perimeter of the island in grid.
    '''
    # If the grid is empty, there is no island, perimeter = 0.
    # if grid is not a list return 0.
    if not grid or not isinstance(grid, list):
        return 0

    # Get the width and height of the grid.
    width, height = len(grid), len(grid[0])
    # Start perimeter at 0.
    islands = 0
    neighbors = 0
    # Traverse through the grid index by index.
    for i in range(width):
        for j in range(height):
            # If 1, add number of 0s around 1 to perimeter.
            if grid[i][j] == 1:
                islands += 1
                if i - 1 >= 0 and grid[i - 1][j]:
                    neighbors += 1
                if j - 1 >= 0 and grid[i][j - 1]:
                    neighbors += 1
    return islands * 4 - neighbors * 2
