import numpy as np


def trapezoidal_rule(func, a, b, subintervals):
    """
    Trapezoidal Rule for Numerical Integration.

    Approximates the definite integral of a function over [a, b]
    using the trapezoidal rule with the specified number of subintervals.

    Parameters:
    func (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    subintervals (int): The number of subintervals (must be >= 1).

    Returns:
    float: The approximate definite integral.

    Raises:
    ValueError: If input arguments are invalid.
    """


    if not isinstance(subintervals, int):
        raise ValueError("The segment can only be divided into whole numbers.")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("a and b must be numbers.")

    if not callable(func):
        raise ValueError("func must be a function.")

    if b <= a:
        raise ValueError("b must be bigger then a.")

    if subintervals < 1:
        raise ValueError("The segment cannot be divided by less than 1.")


    height = (b - a) / subintervals
    integral = 0.5 * (func(a) + func(b))  # Initialize with endpoints

    for i in range(1, subintervals):
        x_i = a + i * height
        integral += func(x_i)

    integral *= height

    return integral


def simpsons_rule(func, a, b, subintervals):
    """
    Simpson's Rule for Numerical Integration.

    Approximates the definite integral of a function over [a, b]
    using Simpson's rule with the specified number of subintervals.
    The number of subintervals must be even and at least 2.

    Parameters:
    func (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    subintervals (int): The number of subintervals (must be even and >= 2).

    Returns:
    float: The approximate definite integral.

    Raises:
    ValueError: If input arguments are invalid.
    """

    if not isinstance(subintervals, int):
        raise ValueError("The segment can only be divided into whole numbers.")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("a and b must be numbers.")

    if not callable(func):
        raise ValueError("func must be a function.")

    if b <= a:
        raise ValueError("b must be bigger then a.")

    if subintervals % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    if subintervals < 2:
        raise ValueError("Number of subintervals (n) must be at least 2.")

    height = (b - a) / subintervals

    integral = func(a) + func(b)  # Initialize with endpoints

    for i in range(1, subintervals):
        x_i = a + i * height
        if i % 2 == 0:
            integral += 2 * func(x_i)
        else:
            integral += 4 * func(x_i)

    integral *= height / 3

    return integral


def romberg_integration(func, a, b, iterations):
    """
    Romberg Integration for Numerical Integration.

    Uses Richardson extrapolation to approximate the definite integral
    of a function over [a, b] with increasing accuracy over multiple iterations.

    Parameters:
    func (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    iterations (int): The number of Romberg iterations (must be >= 1).

    Returns:
    float: The approximate definite integral.

    Raises:
    ValueError: If input arguments are invalid.
    """

    if not isinstance(iterations, int):
        raise ValueError("n must be an integer.")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("a and b must be numbers.")

    if not callable(func):
        raise ValueError("f must be a function.")

    if b <= a:
        raise ValueError("b must be bigger then a.")

    if iterations < 1:
        raise ValueError("iterations cannot be smaller than 1.")


    height = b - a
    result = np.zeros((iterations, iterations), dtype=float)

    result[0, 0] = 0.5 * height * (func(a) + func(b))

    for i in range(1, iterations):
        height /= 2
        sum_term = 0

        for k in range(1, 2 ** i, 2):
            sum_term += func(a + k * height)

        result[i, 0] = 0.5 * result[i - 1, 0] + height * sum_term

        for j in range(1, i + 1):
            result[i, j] = result[i, j - 1] + (result[i, j - 1] - result[i - 1, j - 1]) / ((4 ** j) - 1)

    return result[iterations - 1, iterations - 1]
