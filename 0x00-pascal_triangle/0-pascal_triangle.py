#!/usr/bin/python3
'''
Defines Pascal's Triangle.
'''


def pascal_triangle(n):
    '''
    Returns a representation of a Pascal's triangle.

    Args:
        n (int): The size of the Pascal triangle.

    Returns:
        A list of list of integers representing the pascal's triangle.
    '''

    triangle = []
    if n > 0:
        for i in range(n):
            row = []
            for j in range(i + 1):
                # If at the start/end of a row append 1.
                if j == 0 or j == i:
                    row.append(1)
                # If not on the first row append appropriate number.
                elif i > 0 and j > 0:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            # Append row to triangle.
            triangle.append(row)

    return triangle
