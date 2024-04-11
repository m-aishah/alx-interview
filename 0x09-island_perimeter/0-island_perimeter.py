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
    perimeter = 0
    # Traverse through the grid index by index.
    for i in range(width):
        for j in range(height):
            # If there is land, add the number of 0s around the land to perimeter.
            if grid[i][j] == 1:
                if i in (0, width - 1):
                    perimeter += 1
                if j in (0, height - 1):
                    perimeter += 1
                perimeter = perimeter + int(not grid[i][j - 1]) + int(
                    not grid[i][j + 1]) + int(not grid[i - 1][j]) + int(not grid[i + 1][j])
    return perimeter
