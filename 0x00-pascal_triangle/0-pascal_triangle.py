#!/usr/bin/python3
# pascal_triangle.py

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Pascal's triangle is a triangular array of integers in which the first and last elements of each row are 1,
    and each of the other elements is the sum of the two elements immediately above it in the previous row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Each inner list corresponds to a row of the triangle, containing the elements as integers.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
