#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in a grid.

    The grid is a 2D list where:
    - 1 represents land
    - 0 represents water

    Args:
    grid (list of list of int): The 2D grid representing the map.

    Returns:
    int: The perimeter of the island.
    """
    side = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if j == 0 or grid[i][j - 1] == 0:
                    side += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    side += 1
                if i == 0 or grid[i - 1][j] == 0:
                    side += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    side += 1

    return side
