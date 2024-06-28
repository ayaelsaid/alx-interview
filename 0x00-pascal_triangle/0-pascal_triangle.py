#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for k in range(1, n):
        last_row = triangle[-1]
        new_line = [1]
        
        for i in range(1, k):
            new_line.append(last_row[i - 1] + last_row[i])
        
        new_line.append(1)
        triangle.append(new_line)
    
    return triangle
