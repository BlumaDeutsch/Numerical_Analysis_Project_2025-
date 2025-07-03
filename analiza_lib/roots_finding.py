def Newton_Raphson(func, f_prime, x0, epsilon=0.0001, max_iter=100):
    """
    Newton-Raphson Method for finding a root of a function.

    Parameters:
    func (function): The function for which the root is to be found.
    f_prime (function): The derivative of the function.
    x0 (float): Initial guess for the root.
    epsilon (float, optional): Desired precision. Defaults to 0.0001.
    max_iter (int, optional): Maximum number of iterations. Defaults to 100.

    Returns:
    float: Estimated root if found within the specified tolerance.

    Raises:
    ValueError: If input arguments are invalid or if the method does not converge.
    Exception: For any unexpected runtime errors.
    """

    if not callable(func):
        raise ValueError("func must be a function.")

    if not callable(f_prime):
        raise ValueError("func must be a function.")

    if not isinstance(x0, (int, float)):
        raise ValueError("x0 must be a number")

    if not isinstance(epsilon, (int, float)) or epsilon <= 0:
        raise ValueError("epsilon must be a positive number.")

    if not isinstance(max_iter, int) or max_iter <= 0:
        raise ValueError("max_iter must be a positive integer.")

    iteration = 0
    x = x0
    try:
        while iteration < max_iter:
            fx = func(x)
            fpx = f_prime(x)

            if fpx == 0:
                raise ValueError("Derivative equals 0. Cannot continue.")

            x_new = x - fx / fpx
            iteration += 1

            if abs(x_new - x) < epsilon:
                print(f"Estimated root: {x_new}")
                print(f"Number of iterations: {iteration}")
                return x_new

            x = x_new

        raise ValueError("The method did not converge after 100 iterations.")

    except Exception as e:
        print("Unexpected error: ", e)
        raise


def Bisection_Method(func, a, b, epsilon=0.0001, max_iter=100):
    """
    Bisection Method for finding a root of a function within a given interval.

    Parameters:
    func (function): The function for which the root is to be found.
    a (float): Start of the interval.
    b (float): End of the interval.
    epsilon (float, optional): Desired precision. Defaults to 0.0001.
    max_iter (int, optional): Maximum number of iterations. Defaults to 100.

    Returns:
    float: Estimated root if found within the specified tolerance.

    Raises:
    ValueError: If input arguments are invalid, the function does not change sign,
                or if the method does not converge.
    Exception: For any unexpected runtime errors.
    """

    if not callable(func):
        raise ValueError("func must be a function.")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("a and b must be numbers.")

    if not isinstance(epsilon, (int, float)) or epsilon <= 0:
        raise ValueError("epsilon must be a positive number.")

    if not isinstance(max_iter, int) or max_iter <= 0:
        raise ValueError("max_iter must be a positive integer.")


    try:
        if func(a) * func(b) >= 0:
            raise ValueError("The function must change sign in the given range.")

        iteration = 0
        while (b - a) / 2.0 > epsilon and iteration < max_iter:
            midpoint = (a + b) / 2.0
            f_mid = func(midpoint)
            iteration += 1

            if abs(f_mid) < epsilon:
                break

            if func(a) * f_mid < 0:
                b = midpoint
            else:
                a = midpoint

        root = (a + b) / 2.0
        print(f"Bisection Method: Approximate root = {root}")
        print(f"Iterations = {iteration}")
        return root
    except Exception as e:
        print("Unexpected error: ", e)
        raise


def Secant_Method(func, x0, x1, epsilon=0.0001, max_iter=100):
    """
    Secant Method for finding a root of a function using two initial approximations.

    Parameters:
    func (function): The function for which the root is to be found.
    x0 (float): First initial guess.
    x1 (float): Second initial guess.
    epsilon (float, optional): Desired precision. Defaults to 0.0001.
    max_iter (int, optional): Maximum number of iterations. Defaults to 100.

    Returns:
    float: Estimated root if found within the specified tolerance.

    Raises:
    ValueError: If input arguments are invalid or if the method does not converge.
    ZeroDivisionError: If a division by zero occurs during iteration.
    Exception: For any unexpected runtime errors.
    """

    if not callable(func):
        raise ValueError("func must be a function.")

    if not isinstance(x0, (int, float)) or not isinstance(x1, (int, float)):
        raise ValueError("a and b must be numbers.")

    if not isinstance(epsilon, (int, float)) or epsilon <= 0:
        raise ValueError("epsilon must be a positive number.")

    if not isinstance(max_iter, int) or max_iter <= 0:
        raise ValueError("max_iter must be a positive integer.")

    iteration = 0
    try:
        while iteration < max_iter:
            f_x0 = func(x0)
            f_x1 = func(x1)

            denominator = f_x1 - f_x0
            if denominator == 0:
                raise ZeroDivisionError("division by zero.")

            x2 = x1 - f_x1 * (x1 - x0) / denominator
            iteration += 1

            if abs(x2 - x1) < epsilon:
                print(f"Secant Method: Approximate root = {x2}")
                print(f"Iterations = {iteration}")
                return x2

            x0, x1 = x1, x2

        raise ValueError("The method did not converge after maximum iterations.")
    except Exception as e:
        print("Unexpected error: ", e)
        raise
