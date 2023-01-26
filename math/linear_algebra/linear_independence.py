import numpy as np


def check_linear_independence(vectors):
    matrix = np.column_stack(vectors)
    rref, _ = np.linalg.qr(matrix)
    if np.all(rref[np.where(rref != 0)] == 1):
        return "Linearly Independent"
    else:
        return "Linearly Dependent"


if __name__ == '__main__':
    vectors = [[1, 2], [3, 4], [5, 6]]
    print(check_linear_independence(vectors))
