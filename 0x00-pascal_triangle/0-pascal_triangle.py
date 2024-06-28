#!/usr/bin/python3
'''function that prints pascal_triangle'''

def pascal_triangle(n):
    """
    Print Pascal's triangle up to n rows.

    Parameters:
    n (int): Number of rows in Pascal's triangle to print.

    Returns:
    None
    """
    pascal_triangle = list()  # Initialize Pascal's triangle as an empty list
    
    if n <= 0:
        return pascal_triangle

    # Add first row [1]
    pascal_triangle.append([1])

    # Add second row [1, 1]
    if n > 1:
        pascal_triangle.append([1, 1])

    # Add subsequent rows
    for x in range(3, n + 1):
        new_row = [0] * x
        new_row[0] = 1  # Set first element to 1
        new_row[-1] = 1  # Set last element to 1

        # Calculate middle elements
        for y in range(1, x - 1):
            new_row[y] = pascal_triangle[x - 2][y - 1] + pascal_triangle[x - 2][y]

        pascal_triangle.append(new_row)

    return pascal_triangle
