#!/usr/bin/python3
''' Rotate 2D Matrix '''


def rotate_2d_matrix(matrix):
    '''
    Rotate two dimension matrix 90 degrees clockwise
    '''
    n = len(matrix)
    for x in range(int(n / 2)):
        a = (n - x - 1)
        for y in range(x, a):
            b = (n - 1 - y)
            tmp = matrix[x][y]
            matrix[x][y] = matrix[b][x]
            matrix[b][x] = matrix[a][b]
            matrix[a][b] = matrix[y][a]
            matrix[y][a] = tmp
