#!/usr/bin/python3
'''function that prints pascal_triangle'''


def pascal_triangle(n):
    """
    Print Pascal's triangle up to n rows.

    Parameters:
    n (int): Number of rows in Pascal's triangle to print.

    Returns:
    list: triangle represented as a list of lists
    """
    triangle = list()  # Initialize triangle as an empty list

    if n <= 0:
        return triangle

    # Add first row [1]
    triangle.append([1])

    # Add second row [1, 1]
    if n > 1:
        triangle.append([1, 1])

    # Add subsequent rows
    for x in range(3, n + 1):
        row = [0] * x
        row[0] = 1  # Set first element to 1
        row[-1] = 1  # Set last element to 1

        # Calculate middle elements
        for y in range(1, x - 1):
            row[y] = triangle[x - 2][y - 1] + triangle[x - 2][y]

        triangle.append(row)

    return triangle
