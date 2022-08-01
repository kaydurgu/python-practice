
import math


class MaxPooling:
    def __init__(self, step, size) -> None:
        self.step = step
        self.size = size
    
    @staticmethod
    def checkout(matrix):
        lengths = [len(matrix[i]) for i in range(len(matrix))]
        if len(set(lengths))> 1:
            raise ValueError("Неверный формат для первого параметра matrix.")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if type(matrix[i][j]) not in (float, int):
                    raise ValueError("Неверный формат для первого параметра matrix.")

    def __call__(self, matrix ,*args, **kwargs):
        self.checkout(matrix)
        new_matrix = []
        for i in range(0,len(matrix), self.step[0]):
            row = []
            for j in range(0,len(matrix[0]), self.step[1]):
                if (i + self.size[0]) - 1 >= len(matrix) or (j + self.size[1]) - 1 >=len(matrix[0]):
                    continue
                mx = -math.inf
                for k in range(i, i+self.size[0]):
                    for g in range(j, j + self.size[1]):
                        mx = max(mx , matrix[k][g])
                row.append(mx)
            if row:
                new_matrix.append(row)
        return new_matrix
