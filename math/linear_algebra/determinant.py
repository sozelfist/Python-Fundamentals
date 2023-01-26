def determinant(A):
    """
    Calculate the determinant of a matrix A
    """
    if len(A) != len(A[0]):
        raise ValueError("The matrix is not square, determinant not defined")
    # base case for 2x2 matrix
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]

    # find matrix of cofactors
    cofactors = []
    for c in range(len(A)):
        cofactorRow = []
        for r in range(len(A)):
            minor = [row[:c] + row[c + 1:] for row in (A[:r] + A[r + 1:])]
            cofactorRow.append((-1)**(r + c) * determinant(minor))
        cofactors.append(cofactorRow)
    # find the determinant
    det = sum(A[i][0] * cofactors[i][0] for i in range(len(A)))
    return det


if __name__ == '__main__':
    print('Determinant: ', determinant([[2, 1, 5], [1, 2, 7], [8, 9, 10]]))
