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
    if n <= 0:
        return
    
    triangle = [[1]]  # Initialize the triangle with the first row [1]
    
    for k in range(1, n):
        last_row = triangle[-1]
        new_line = [1]  # First element of each row is always 1
        
        for i in range(1, k):
            new_line.append(last_row[i - 1] + last_row[i])
        
        new_line.append(1)  # Last element of each row is always 1
        triangle.append(new_line)
    
    return triangle
