def linear_interpolation(x_vals, y_vals, x):
    """
    Performs linear interpolation for a given point x using x_vals and y_vals.

    Args:
        x_vals (list): list of x data points (must be sorted in ascending order)
        y_vals (list): corresponding y values
        x (float): the x value to interpolate

    Returns:
        float: interpolated y value

    Raises:
        ValueError: for invalid input or out-of-bounds x
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("x and y lists must be the same length")
    if len(x_vals) < 2:
        raise ValueError("At least two data points are required for linear interpolation")
    if x < x_vals[0] or x > x_vals[-1]:
        raise ValueError("The point is outside the range of the table")

    for i in range(len(x_vals) - 1):
        if x_vals[i] <= x <= x_vals[i + 1]:
            x0, x1 = x_vals[i], x_vals[i + 1]
            y0, y1 = y_vals[i], y_vals[i + 1]
            return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

    raise ValueError("Could not interpolate the given value")


def polynomial_interpolation(x_vals, y_vals, x):
    """
    Performs polynomial interpolation using Lagrange method.

    Args:
        x_vals (list): list of x data points
        y_vals (list): corresponding y values
        x (float): the x value to interpolate

    Returns:
        float: interpolated y value

    Raises:
        ValueError: for invalid input, duplicate x values, or out-of-bounds x
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("x and y lists must be the same length")
    if len(x_vals) == 0:
        raise ValueError("At least one data point is required for polynomial interpolation")
    if x < min(x_vals) or x > max(x_vals):
        raise ValueError("The point is outside the range of the table")

    result = 0
    n = len(x_vals)

    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if j != i:
                if x_vals[i] == x_vals[j]:
                    raise ValueError("Duplicate x values are not allowed")
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        result += term
    return result


def lagrange_interpolation(x_vals, y_vals, x):
    """
    Lagrange Interpolation.

    Computes an interpolated y-value for a given x using the Lagrange
    interpolation formula.

    Parameters:
        x_vals (list of float): List of x data points.
        y_vals (list of float): Corresponding y-values.
        x (float): The x-value to interpolate.

    Returns:
        float: The interpolated y-value at the given x.

    Raises:
        ValueError: If inputs are invalid, lists are mismatched, or x-values are duplicated.
    """

    n = len(x_vals)
    result = 0.0

    if n < 2:
        raise ValueError("At least two data points are required")

    if n != len(y_vals):
        raise ValueError("x points and y points must be the same length")

    try:
        x_vals = [float(xi) for xi in x_vals]
        y_vals = [float(yi) for yi in y_vals]
        x = float(x)
    except ValueError:
        raise ValueError("x points, y points, and x must contain numeric values")

    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                if x_vals[i] == x_vals[j]:
                    raise ValueError("There are 2 x points with the same value")
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        result += term
    return result


def neville(x_vals, y_vals, x_interpolate):
    """
    Neville's Method for Polynomial Interpolation.

    Computes an interpolated y-value for a given x using Neville's algorithm.

    Parameters:
        x_vals (list of float): List of x data points.
        y_vals (list of float): Corresponding y-values.
        x_interpolate (float): The x-value to interpolate.

    Returns:
        float: The interpolated y-value at the given x.

    Raises:
        ValueError: If inputs are invalid, lists are mismatched, or x-values are duplicated.
    """

    n = len(x_vals)

    if n < 2:
        raise ValueError("At least two data points are required")

    if n != len(y_vals):
        raise ValueError("x points and y points must be the same length")

    try:
        x_vals = [float(xi) for xi in x_vals]
        y_vals = [float(yi) for yi in y_vals]
        x_interpolate = float(x_interpolate)
    except ValueError:
        raise ValueError("x points, y points, and x_interpolate must contain numeric values")


    # Initialize the tableau
    tableau = [[0.0] * n for _ in range(n)]
    for i in range(n):
        tableau[i][0] = y_vals[i]
    for j in range(1, n):
        for i in range(n - j):
            if x_vals[i] == x_vals[i + j]:
                raise ValueError("There are 2 x points with the same value")
            tableau[i][j] = ((x_interpolate - x_vals[i + j]) * tableau[i][j - 1] -
                             (x_interpolate - x_vals[i]) * tableau[i + 1][j - 1]) / (x_vals[i] - x_vals[i + j])

    return tableau[0][n - 1]


def cubic_spline_interpolation(x_vals, y_vals, x_interp):
    """
    Cubic Spline Interpolation.

    Computes an interpolated y-value for a given x using a natural cubic spline.

    Parameters:
        x_vals (list of float): Sorted list of x data points.
        y_vals (list of float): Corresponding y-values.
        x_interp (float): The x-value to interpolate.

    Returns:
        float: The interpolated y-value at the given x.

    Raises:
        ValueError: If inputs are invalid, lists are mismatched, x-values are not sorted, or x is out of bounds.
    """

    try:
        # Input validations
        if len(x_vals) != len(y_vals):
            raise ValueError("x and y lists must be the same length.")
        if len(x_vals) < 3:
            raise ValueError("At least three data points are required.")
        if sorted(x_vals) != x_vals:
            raise ValueError("x values must be sorted in ascending order.")
        if not isinstance(x_interp, (int, float)):
            raise ValueError("x_interp must be a numeric value.")
        if x_interp < x_vals[0] or x_interp > x_vals[-1]:
            raise ValueError("x_interp is outside the interpolation range.")

        # Step 1: Compute h and alpha
        n = len(x_vals)
        h = [x_vals[i + 1] - x_vals[i] for i in range(n - 1)]
        alpha = [
            (3 / h[i]) * (y_vals[i + 1] - y_vals[i]) -
            (3 / h[i - 1]) * (y_vals[i] - y_vals[i - 1])
            for i in range(1, n - 1)
        ]

        # Step 2: Solve tridiagonal system for c
        l = [1] + [0] * (n - 1)
        mu = [0] * n
        z = [0] * n

        for i in range(1, n - 1):
            l[i] = 2 * (x_vals[i + 1] - x_vals[i - 1]) - h[i - 1] * mu[i - 1]
            mu[i] = h[i] / l[i]
            z[i] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]

        l[-1] = 1
        z[-1] = 0

        c = [0] * n
        b = [0] * (n - 1)
        d = [0] * (n - 1)
        a = y_vals[:-1]

        for j in range(n - 2, -1, -1):
            c[j] = z[j] - mu[j] * c[j + 1]
            b[j] = ((y_vals[j + 1] - y_vals[j]) / h[j]) - (h[j] * (c[j + 1] + 2 * c[j]) / 3)

            d[j] = (c[j + 1] - c[j]) / (3 * h[j])

        # Step 3: Find the interval and interpolate
        for i in range(n - 1):
            if x_vals[i] <= x_interp <= x_vals[i + 1]:
                dx = x_interp - x_vals[i]
                return a[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3

    except Exception as e:
        return f"Error: {e}"
