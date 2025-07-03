import numpy as np


def is_dominant_diagonal(matrix):
    """
    Check if a matrix has a dominant diagonal.

    A matrix is diagonally dominant if for each row, the magnitude of the diagonal
    element is greater than or equal to the sum of the magnitudes of the other elements.

    Parameters:
        matrix (list of list of float): Coefficient matrix.

    Returns:
        bool: True if the matrix is diagonally dominant, False otherwise.
    """

    for i in range(len(matrix)):
        if abs(matrix[i][i]) < sum(abs(matrix[i][j]) for j in range(len(matrix)) if j != i):
            return False
    return True


def attempt_fix_dominant_diagonal(matrix):
    """
    Attempt to rearrange rows of a matrix to achieve diagonal dominance.

    If rearrangement is not possible, the original matrix is returned.

    Parameters:
        matrix (list of list of float): Coefficient matrix.

    Returns:
        list of list of float: Rearranged matrix if possible.
    """

    size = len(matrix)
    assigned_cols = [-1]*size
    new_matrix = [None]*size

    for i in range(size):
        for j in range(size):
            if abs(matrix[i][j]) >= sum(abs(matrix[i][k]) for k in range(size) if k != j):
                if assigned_cols.count(j) == 0:
                    assigned_cols[i] = j
                    break

    if -1 in assigned_cols:
        print("Could not find a dominant diagonal.")
        return matrix

    for i in range(size):
        new_matrix[assigned_cols[i]] = matrix[i]

    return new_matrix


def max_norm_matrix(matrix):
    """
    Calculate the infinity norm (maximum row sum) of a matrix.

    Parameters:
        matrix (numpy.ndarray or list of lists): The input matrix.

    Returns:
        float: The infinity norm.
    """
    max_row_sum = 0
    for row in matrix:
        row_sum = sum(abs(x) for x in row)
        max_row_sum = max(max_row_sum, row_sum)
    return max_row_sum


def row_addition_elementary_matrix(n, target_row, source_row, scalar=1.0):
    """
    Create an elementary matrix for adding a multiple of one row to another.

    Parameters:
        n (int): Size of the square matrix.
        target_row (int): Index of the row to be modified.
        source_row (int): Index of the row to be added.
        scalar (float, optional): Multiple of the source row to add (default is 1.0).

    Returns:
        numpy.ndarray: The elementary matrix.

    Raises:
        ValueError: For invalid indices or if source and target rows are the same.
    """

    if target_row < 0 or source_row < 0 or target_row >= n or source_row >= n:
        raise ValueError("Invalid row indices.")

    if target_row == source_row:
        raise ValueError("Source and target rows cannot be the same.")

    elementary_matrix = np.identity(n)
    elementary_matrix[target_row, source_row] = scalar

    return np.array(elementary_matrix)


def scalar_multiplication_elementary_matrix(n, row_index, scalar):
    """
    Create an elementary matrix for scaling a row by a scalar.

    Parameters:
        n (int): Size of the square matrix.
        row_index (int): Index of the row to scale.
        scalar (float): The scalar to multiply the row by.

    Returns:
        numpy.ndarray: The elementary matrix.

    Raises:
        ValueError: For invalid index or zero scalar.
    """

    if row_index < 0 or row_index >= n:
        raise ValueError("Invalid row index.")

    if scalar == 0:
        raise ValueError("Scalar cannot be zero for row multiplication.")

    elementary_matrix = np.identity(n)
    elementary_matrix[row_index, row_index] = scalar

    return np.array(elementary_matrix)


def matrix_inverse(matrix):
    """
    Compute the inverse of a square matrix using elementary row operations.

    Prints step-by-step transformations for educational purposes.

    Parameters:
        matrix (numpy.ndarray): The square matrix to invert.

    Returns:
        numpy.ndarray: The inverse of the matrix.

    Raises:
        ValueError: If the matrix is not square or is singular.
    """

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        if matrix[i, i] == 0:
            raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")
            matrix = np.dot(elementary_matrix, matrix)
            print(f"The matrix after elementary operation :\n {matrix}")
            print("------------------------------------------------------------------------------------------------------------------")
            identity = np.dot(elementary_matrix, identity)

        # Zero out the elements above and below the diagonal
        for j in range(n):
            if i != j:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print( "------------------------------------------------------------------------------------------------------------------")
                identity = np.dot(elementary_matrix, identity)

    return identity
