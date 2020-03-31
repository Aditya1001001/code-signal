"""You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Note: Try to solve this task in-place (with O(1) additional memory), since this
is what you'll be asked to do during an interview.

asked by- Amazon, Microsoft, Apple

Example:
For
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be
rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]"""

def rotateImage(a):
    height, width = len(a), len(a[0])
    for i in range(height):
        for j in range(width):
            if i == j:
                break
            a[i][j], a[j][i] = a[j][i], a[i][j]
    x = width // 2
    for i in range(height):
        for j in range(x):
            a[i][j], a[i][width - j - 1] = a[i][width - j - 1], a[i][j]
    return a