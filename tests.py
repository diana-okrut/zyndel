from unittest import TestCase

import numpy as np

from matrix_updater import update_matrix


class TestCreateUpdatedMatrix(TestCase):

    def test_with_unit_1Xyes(self):
        expected = ([[-1., -1., -1., -1., -1.],
                     [-1., 1., -1., -1., -1.],
                     [-1., 1., 1., -1., -1.],
                     [-1., 1., 1., 1., -1.],
                     [-1., 1., 1., 1., 1.]])
        actual = update_matrix(np.zeros((5, 5)), -1.0, 1.0, '1X&&yes')
        self.assertTrue(np.array_equal(actual, expected))

    def test_with_unit_1Xno(self):
        expected = ([[1., 1., 1., 1., 1.],
                     [1., -1., 1., 1., 1.],
                     [1., -1., -1., 1., 1.],
                     [1., -1., -1., -1., 1.],
                     [1., -1., -1., -1., -1.]])
        actual = update_matrix(np.zeros((5, 5)), -1.0, 1.0, '1X&&no')
        self.assertTrue(np.array_equal(actual, expected))

    def test_with_unit_12yes(self):
        expected = ([[-1., -1., -1., -1., -1.],
                     [-1., -1., 1., 1., 1.],
                     [-1., 1., -1., 1., 1.],
                     [-1., 1., 1., -1., 1.],
                     [-1., 1., 1., 1., -1.]])
        actual = update_matrix(np.zeros((5, 5)), -1.0, 1.0, '12&&yes')
        self.assertTrue(np.array_equal(actual, expected))

    def test_with_unit_12no(self):
        expected = ([[1., 1., 1., 1., 1.],
                     [1., 1., -1., -1., -1.],
                     [1., -1., 1., -1., -1.],
                     [1., -1., -1., 1., -1.],
                     [1., -1., -1., -1., 1.]])
        actual = update_matrix(np.zeros((5, 5)), -1.0, 1.0, '12&&no')
        self.assertTrue(np.array_equal(actual, expected))

    def test_with_unit_2Xyes(self):
        expected = ([[-1., -1., -1., -1., -1.],
                     [-1., 1., 1., 1., 1.],
                     [-1., -1., 1., 1., 1.],
                     [-1., -1., -1., 1., 1.],
                     [-1., -1., -1., -1., 1.]])
        actual = update_matrix(np.zeros((5, 5)), -1.0, 1.0, '2X&&yes')
        self.assertTrue(np.array_equal(actual, expected))

    def test_with_unit_2Xno(self):
        expected = ([[1., 1., 1., 1., 1.],
                     [1., -1., -1., -1., -1.],
                     [1., 1., -1., -1., -1.],
                     [1., 1., 1., -1., -1.],
                     [1., 1., 1., 1., -1.]])
        actual = update_matrix(np.zeros((5, 5)), -1.0, 1.0, '2X&&no')
        self.assertTrue(np.array_equal(actual, expected))
