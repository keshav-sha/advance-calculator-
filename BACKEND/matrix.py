import numpy as np


class MatrixCalculator:

    @staticmethod
    def add(matrix1, matrix2):
        return (np.array(matrix1) + np.array(matrix2)).tolist()

    @staticmethod
    def subtract(matrix1, matrix2):
        return (np.array(matrix1) - np.array(matrix2)).tolist()

    @staticmethod
    def multiply(matrix1, matrix2):
        return np.matmul(matrix1, matrix2).tolist()

    @staticmethod
    def transpose(matrix):
        return np.transpose(matrix).tolist()

    @staticmethod
    def determinant(matrix):
        return float(np.linalg.det(matrix))

    @staticmethod
    def inverse(matrix):
        return np.linalg.inv(matrix).tolist()

    @staticmethod
    def rank(matrix):
        return int(np.linalg.matrix_rank(matrix))