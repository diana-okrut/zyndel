import numpy as np


def update_matrix(matrix, S, Cf, unit):
    matrix = matrix + np.ones((5, 5)) * S
    line, column = np.mgrid[0:matrix.shape[0], 0:matrix.shape[1]]
    if unit == "1X&&yes":
        matrix[np.logical_and(np.logical_and(line > 0, column > 0), line >= column)] *= -Cf

    elif unit == "1X&&no":
        matrix[np.logical_or(np.logical_or(line < 0, column == 0), line < column)] *= -Cf

    elif unit == "12&&yes":
        matrix[np.logical_and(np.logical_and(line > 0, column > 0), line != column)] *= -Cf

    elif unit == "12&&no":
        matrix[np.logical_or(np.logical_or(line == 0, column == 0), line == column)] *= -Cf

    elif unit == "2X&&yes":
        matrix[np.logical_and(np.logical_and(line > 0, column > 0), line <= column)] *= -Cf

    elif unit == "2X&&no":
        matrix[np.logical_or(np.logical_or(line == 0, column == 0), line > column)] *= -Cf

    return matrix


if __name__ == '_main__':
    update_matrix(np.zeros((5, 5)), 0.13, 0.45, "1X&&yes")
