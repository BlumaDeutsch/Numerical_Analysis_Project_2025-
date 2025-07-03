import numpy as np

from analiza_lib.help_functions import is_dominant_diagonal, attempt_fix_dominant_diagonal, max_norm_matrix, matrix_inverse


def jacobi_solver(coefficients, constants, tol, previous_guess, iteration=1):
    """
    Solve a system of linear equations using the Jacobi iterative method.

    The method checks for diagonal dominance and attempts to rearrange
    the coefficient matrix if needed. Iterations continue until the
    solution converges within the specified tolerance.

    Parameters:
        coefficients (list of list of float): Coefficient matrix A.
        constants (list of float): Right-hand side vector b.
        tol (float): Convergence tolerance for stopping criteria.
        previous_guess (list of float): Initial guess for the solution.
        iteration (int, optional): Iteration counter (default is 1).

    Returns:
        None

    Raises:
        ValueError: If the system cannot converge or if inputs are invalid.
    """

    # if not is_dominant_diagonal(coefficients):
    #     print("\nNo dominant diagonal detected. Attempting to rearrange...")
    #     coefficients = attempt_fix_dominant_diagonal(coefficients)
    #     if not is_dominant_diagonal(coefficients):
    #         print("\nWarning: Still no dominant diagonal. Convergence is not guaranteed.\n")
    #
    # next_guess = []
    # for i in range(len(coefficients)):
    #     sum_other = sum(coefficients[i][j]*previous_guess[j] for j in range(len(coefficients)) if i != j)
    #     next_val = (constants[i] - sum_other)/coefficients[i][i]
    #     next_guess.append(next_val)
    #
    # print(f"Iteration {iteration}: {next_guess}")
    #
    # if all(abs(next_guess[i] - previous_guess[i]) < tol for i in range(len(coefficients))):
    #     print(f"\nTotal Iterations: {iteration}")
    #     return
    #
    # jacobi_solver(coefficients, constants, tol, next_guess, iteration+1)

    if not isinstance(coefficients, list) or not all(isinstance(row, list) for row in coefficients):
        raise ValueError("coefficients must be a list of lists.")

    n = len(coefficients)
    if any(len(row) != n for row in coefficients):
        raise ValueError("Coefficient matrix must be square.")

    if not isinstance(constants, list) or len(constants) != n:
        raise ValueError("constants must be a list of length equal to the number of equations.")

    if not isinstance(previous_guess, list) or len(previous_guess) != n:
        raise ValueError("previous_guess must be a list of length equal to the number of variables.")

    if not isinstance(tol, (int, float)) or tol <= 0:
        raise ValueError("tol must be a positive number.")

    if not isinstance(iteration, int) or iteration < 1:
        raise ValueError("iteration must be a positive integer.")

    # === Diagonal dominance check ===
    if not is_dominant_diagonal(coefficients):
        print("\nNo dominant diagonal detected. Attempting to rearrange...")
        coefficients = attempt_fix_dominant_diagonal(coefficients)
        if not is_dominant_diagonal(coefficients):
            print("\nWarning: Still no dominant diagonal. Convergence is not guaranteed.\n")

    # === Iteration ===
    next_guess = []
    for i in range(len(coefficients)):
        sum_other = sum(coefficients[i][j]*previous_guess[j] for j in range(len(coefficients)) if i != j)
        next_val = (constants[i] - sum_other)/coefficients[i][i]
        next_guess.append(next_val)

    print(f"Iteration {iteration}: {next_guess}")

    if all(abs(next_guess[i] - previous_guess[i]) < tol for i in range(len(coefficients))):
        print(f"\nTotal Iterations: {iteration}")
        return

    jacobi_solver(coefficients, constants, tol, next_guess, iteration+1)


def gauss_seidel_solver(coefficients, constants, tol, previous_guess, iteration=1):
    """
    Solve a system of linear equations using the Gauss-Seidel iterative method.

    The method checks for diagonal dominance and attempts to rearrange
    the coefficient matrix if needed. Updates are applied immediately
    within each iteration for faster convergence than Jacobi.

    Parameters:
        coefficients (list of list of float): Coefficient matrix A.
        constants (list of float): Right-hand side vector b.
        tol (float): Convergence tolerance for stopping criteria.
        previous_guess (list of float): Initial guess for the solution.
        iteration (int, optional): Iteration counter (default is 1).

    Returns:
        None

    Raises:
        ValueError: If the system cannot converge or if inputs are invalid.
    """

    # if not is_dominant_diagonal(coefficients):
    #     print("\nNo dominant diagonal detected. Attempting to rearrange...")
    #     coefficients = attempt_fix_dominant_diagonal(coefficients)
    #     if not is_dominant_diagonal(coefficients):
    #         print("\nWarning: Still no dominant diagonal. Convergence is not guaranteed.\n")
    #
    # current_guess = previous_guess.copy()
    #
    # for i in range(len(coefficients)):
    #     sum_other = sum(coefficients[i][j]*current_guess[j] for j in range(len(coefficients)) if i != j)
    #     current_guess[i] = (constants[i] - sum_other)/coefficients[i][i]
    #
    # print(f"Iteration {iteration}: {current_guess}")
    #
    # if all(abs(current_guess[i] - previous_guess[i]) < tol for i in range(len(coefficients))):
    #     print(f"\nTotal Iterations: {iteration}")
    #     return
    #
    # gauss_seidel_solver(coefficients, constants, tol, current_guess, iteration+1)

    if not isinstance(coefficients, list) or not all(isinstance(row, list) for row in coefficients):
        raise ValueError("coefficients must be a list of lists.")

    n = len(coefficients)
    if any(len(row) != n for row in coefficients):
        raise ValueError("Coefficient matrix must be square.")

    if not isinstance(constants, list) or len(constants) != n:
        raise ValueError("constants must be a list of length equal to the number of equations.")

    if not isinstance(previous_guess, list) or len(previous_guess) != n:
        raise ValueError("previous_guess must be a list of length equal to the number of variables.")

    if not isinstance(tol, (int, float)) or tol <= 0:
        raise ValueError("tol must be a positive number.")

    if not isinstance(iteration, int) or iteration < 1:
        raise ValueError("iteration must be a positive integer.")

    # === Diagonal dominance check ===
    if not is_dominant_diagonal(coefficients):
        print("\nNo dominant diagonal detected. Attempting to rearrange...")
        coefficients = attempt_fix_dominant_diagonal(coefficients)
        if not is_dominant_diagonal(coefficients):
            print("\nWarning: Still no dominant diagonal. Convergence is not guaranteed.\n")

    current_guess = previous_guess.copy()

    for i in range(len(coefficients)):
        sum_other = sum(coefficients[i][j]*current_guess[j] for j in range(len(coefficients)) if i != j)
        current_guess[i] = (constants[i] - sum_other)/coefficients[i][i]

    print(f"Iteration {iteration}: {current_guess}")

    if all(abs(current_guess[i] - previous_guess[i]) < tol for i in range(len(coefficients))):
        print(f"\nTotal Iterations: {iteration}")
        return

    gauss_seidel_solver(coefficients, constants, tol, current_guess, iteration+1)


def condition_number(matrix):
    """
    Compute the condition number of a square matrix using the infinity norm.

    The condition number estimates how sensitive the solution of a linear system
    is to changes in the input or round-off errors.

    Parameters:
        matrix (numpy.ndarray): The square matrix A.

    Returns:
        float: The condition number of the matrix.

    Raises:
        ValueError: If the matrix is not square or not invertible.
    """
    # # Step 1: Calculate the infinity norm of A
    # norm_A = max_norm_matrix(matrix)
    #
    # # Step 2: Calculate the inverse of A
    # matrix_inv = matrix_inverse(matrix)
    #
    # # Step 3: Calculate the infinity norm of the inverse of A
    # norm_A_inv = max_norm_matrix(matrix_inv)
    #
    # # Step 4: Compute the condition number
    # cond = norm_A * norm_A_inv
    #
    # return cond

    if not isinstance(matrix, np.ndarray):
        raise ValueError("Input must be a numpy.ndarray.")

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    norm_A = max_norm_matrix(matrix)
    matrix_inv = matrix_inverse(matrix)
    norm_A_inv = max_norm_matrix(matrix_inv)

    cond = norm_A * norm_A_inv
    return cond


# if __name__ == "__main__":
#     import numpy as np
#
#     # Example system (3x3)
#     coefficients = [
#         [10.0, 2.0, -1.0],
#         [-3.0, -6.0, 2.0],
#         [1.0, 1.0, 5.0]
#     ]
#     constants = [27.0, -61.5, -21.5]
#     initial_guess = [0.0, 0.0, 0.0]
#     tolerance = 1e-5
#
#     print("Testing Jacobi Solver:")
#     jacobi_solver(coefficients, constants, tolerance, initial_guess)
#
#     print("\nTesting Gauss-Seidel Solver:")
#     gauss_seidel_solver(coefficients, constants, tolerance, initial_guess)
#
#     print("\nTesting Condition Number:")
#     matrix = np.array(coefficients, dtype=float)
#     cond_num = condition_number(matrix)
#     print(f"Condition number (infinity norm): {cond_num:.6f}")
