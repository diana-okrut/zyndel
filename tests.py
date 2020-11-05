from unittest import TestCase

import numpy as np

from tz import update_matrix


class TestCreateUpdatedMatrix(TestCase):

    def test_with_unit_1Xyes(self):
        answer = ([[1.5, 1.5, 1.5, 1.5, 1.5],
                   [1.5, -1.5, 1.5, 1.5, 1.5],
                   [1.5, -1.5, -1.5, 1.5, 1.5],
                   [1.5, -1.5, -1.5, -1.5, 1.5],
                   [1.5, -1.5, -1.5, -1.5, -1.5]])
        matrix = np.zeros((5, 5))
        S = 1.5
        Cf = 1.0
        unit = '1X&&yes'
        new_matrix = update_matrix(matrix, S, Cf, unit)
        self.assertEqual(np.all(new_matrix), np.all(answer))

    def test_with_unit_1Xno(self):
        answer = ([[-1.5, -1.5, -1.5, -1.5, -1.5],
                   [-1.5, 1.5, -1.5, -1.5, -1.5],
                   [-1.5, 1.5, 1.5, -1.5, -1.5],
                   [-1.5, 1.5, 1.5, 1.5, -1.5],
                   [-1.5, 1.5, 1.5, 1.5, 1.5]])
        matrix = np.zeros((5, 5))
        S = 1.5
        Cf = 1.0
        unit = '1X&&no'
        new_matrix = update_matrix(matrix, S, Cf, unit)
        self.assertEqual(np.all(new_matrix), np.all(answer))

    def test_with_unit_12yes(self):
        answer = ([[1.5, 1.5, 1.5, 1.5, 1.5],
                   [1.5, 1.5, -1.5, -1.5, -1.5],
                   [1.5, -1.5, 1.5, -1.5, -1.5],
                   [1.5, -1.5, -1.5, 1.5, -1.5],
                   [1.5, -1.5, -1.5, -1.5, 1.5]])
        matrix = np.zeros((5, 5))
        S = 1.5
        Cf = 1.0
        unit = '12&&yes'
        new_matrix = update_matrix(matrix, S, Cf, unit)
        self.assertEqual(np.all(new_matrix), np.all(answer))

    def test_with_unit_12no(self):
        answer = ([[-1.5, -1.5, -1.5, -1.5, -1.5],
                   [-1.5, -1.5, 1.5, 1.5, 1.5],
                   [-1.5, 1.5, -1.5, 1.5, 1.5],
                   [-1.5, 1.5, 1.5, -1.5, 1.5],
                   [-1.5, 1.5, 1.5, 1.5, -1.5]])
        matrix = np.zeros((5, 5))
        S = 1.5
        Cf = 1.0
        unit = '12&&no'
        new_matrix = update_matrix(matrix, S, Cf, unit)
        self.assertEqual(np.all(new_matrix), np.all(answer))

    def test_with_unit_2Xyes(self):
        answer = ([[1.5, 1.5, 1.5, 1.5, 1.5],
                   [1.5, -1.5, -1.5, -1.5, -1.5],
                   [1.5, 1.5, -1.5, -1.5, -1.5],
                   [1.5, 1.5, 1.5, -1.5, -1.5],
                   [1.5, 1.5, 1.5, 1.5, -1.5]])
        matrix = np.zeros((5, 5))
        S = 1.5
        Cf = 1.0
        unit = '2X&&yes'
        new_matrix = update_matrix(matrix, S, Cf, unit)
        self.assertEqual(np.all(new_matrix), np.all(answer))

    def test_with_unit_2Xno(self):
        answer = ([[-1.5, -1.5, -1.5, -1.5, -1.5],
                   [-1.5, 1.5, 1.5, 1.5, 1.5],
                   [-1.5, -1.5, 1.5, 1.5, 1.5],
                   [-1.5, -1.5, -1.5, 1.5, 1.5],
                   [-1.5, -1.5, -1.5, -1.5, 1.5]])
        matrix = np.zeros((5, 5))
        S = 1.5
        Cf = 1.0
        unit = '2X&&no'
        new_matrix = update_matrix(matrix, S, Cf, unit)
        self.assertEqual(np.all(new_matrix), np.all(answer))
