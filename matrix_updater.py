import numpy as np


def update_matrix(matrix: np.ndarray, S: float, Cf: float, unit: str) -> np.ndarray:
    matrix = matrix + np.ones(matrix.shape) * S
    line, column = np.mgrid[0:matrix.shape[0], 0:matrix.shape[1]]
    if unit == "1X&&yes":
        matrix[np.logical_and(np.logical_and(line > 0, column > 0), line >= column)] *= -Cf

    elif unit == "1X&&no":
        matrix[np.logical_or(np.logical_or(line == 0, column == 0), line < column)] *= -Cf

    elif unit == "12&&yes":
        matrix[np.logical_and(np.logical_and(line > 0, column > 0), line != column)] *= -Cf

    elif unit == "12&&no":
        matrix[np.logical_or(np.logical_or(line == 0, column == 0), line == column)] *= -Cf

    elif unit == "2X&&yes":
        matrix[np.logical_and(np.logical_and(line > 0, column > 0), line <= column)] *= -Cf

    elif unit == "2X&&no":
        matrix[np.logical_or(np.logical_or(line == 0, column == 0), line > column)] *= -Cf

    return matrix
