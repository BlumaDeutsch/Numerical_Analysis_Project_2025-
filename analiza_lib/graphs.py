import base64
import io

import matplotlib.pyplot as plt
import numpy as np
from analiza_lib import *

def plot_linear_interpolation_graph(x_vals, y_vals, filename="linear_interpolation.png"):
    """
    Plots and saves a linear interpolation graph.

    Parameters:
        x_vals (list): x data points.
        y_vals (list): corresponding y values.
        filename (str): name of the image file to save the plot.

    Raises:
        ValueError: if x_vals and y_vals have different lengths.
        Exception: for any general error.
    """
    try:
        # Check if lists are the same length
        if len(x_vals) != len(y_vals):
            raise ValueError("x_vals and y_vals must be the same length.")
        
        # Create 300 x values between min and max for smooth plotting
        xs = np.linspace(min(x_vals), max(x_vals), 300)
        
        # Calculate interpolated y values for each x in xs
        ys = [linear_interpolation(x_vals, y_vals, xi) for xi in xs]

        # Create the plot
        plt.figure()
        plt.plot(x_vals, y_vals, 'o', label='Data Points')  # plot original data points as dots
        plt.plot(xs, ys, '-', label='Linear Interpolation')  # plot interpolated line
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Linear Interpolation Graph')
        plt.legend()
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

        # # Save the plot as an image file
        # plt.savefig(filename)
        #
        # # Show the plot on screen
        # plt.show()
        #
        # # Close the plot to free memory
        # plt.close()
    
    except Exception as e:
        print(f"Error in plot_linear_interpolation_graph: {e}")
        raise

def plot_polynomial_interpolation_graph(x_vals, y_vals, filename="polynomial_interpolation.png"):
    """
    Plots and saves a polynomial interpolation graph using the polynomial_interpolation function.

    Parameters:
        x_vals (list): x data points.
        y_vals (list): corresponding y values.
        filename (str): name of the image file to save the plot.

    Raises:
        ValueError: if x_vals and y_vals have different lengths.
        Exception: for any general error.
    """
    try:
        if len(x_vals) != len(y_vals):
            raise ValueError("x_vals and y_vals must be the same length.")

        # Generate 300 x values within the range for smooth plotting
        xs = np.linspace(min(x_vals), max(x_vals), 300)
        
        # Calculate interpolated y values for each x in xs
        ys = [polynomial_interpolation(x_vals, y_vals, xi) for xi in xs]

        # Create the plot
        plt.figure()
        plt.plot(x_vals, y_vals, 'o', label='Data Points')  # plot original data points as dots
        plt.plot(xs, ys, '-', label='Polynomial Interpolation')  # plot interpolated curve
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Polynomial Interpolation Graph')
        plt.legend()
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

        # # Save and show the plot
        # plt.savefig(filename)
        # plt.show()
        # plt.close()

    except Exception as e:
        print(f"Error in plot_polynomial_interpolation_graph: {e}")
        raise

def plot_lagrange_interpolation_graph(x_vals, y_vals, filename="lagrange_interpolation.png"):
    """
    Plots and saves a Lagrange interpolation graph using the lagrange_interpolation function.

    Parameters:
        x_vals (list): x data points.
        y_vals (list): corresponding y values.
        filename (str): name of the image file to save the plot.

    Raises:
        ValueError: if x_vals and y_vals have different lengths.
        Exception: for any general error.
    """
    try:
        if len(x_vals) != len(y_vals):
            raise ValueError("x_vals and y_vals must be the same length.")

        # Generate 300 x values within the range for smooth plotting
        xs = np.linspace(min(x_vals), max(x_vals), 300)
        
        # Calculate interpolated y values for each x in xs
        ys = [lagrange_interpolation(x_vals, y_vals, xi) for xi in xs]

        # Create the plot
        plt.figure()
        plt.plot(x_vals, y_vals, 'o', label='Data Points')  # plot original data points as dots
        plt.plot(xs, ys, '-', label='Lagrange Interpolation')  # plot interpolated curve
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Lagrange Interpolation Graph')
        plt.legend()
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

        # # Save and show the plot
        # plt.savefig(filename)
        # plt.show()
        # plt.close()

    except Exception as e:
        print(f"Error in plot_lagrange_interpolation_graph: {e}")
        raise

def plot_neville_interpolation_graph(x_vals, y_vals, filename="neville_interpolation.png"):
    """
    Plots and saves a Neville interpolation graph using the neville function.

    Parameters:
        x_vals (list): x data points.
        y_vals (list): corresponding y values.
        filename (str): name of the image file to save the plot.

    Raises:
        ValueError: if x_vals and y_vals have different lengths.
        Exception: for any general error.
    """
    try:
        if len(x_vals) != len(y_vals):
            raise ValueError("x_vals and y_vals must be the same length.")

        # Generate 300 x values within the range for smooth plotting
        xs = np.linspace(min(x_vals), max(x_vals), 300)
        
        # Calculate interpolated y values for each x in xs
        ys = [neville(x_vals, y_vals, xi) for xi in xs]

        # Create the plot
        plt.figure()
        plt.plot(x_vals, y_vals, 'o', label='Data Points')  # plot original data points as dots
        plt.plot(xs, ys, '-', label='Neville Interpolation')  # plot interpolated curve
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Neville Interpolation Graph')
        plt.legend()
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

        # # Save and show the plot
        # plt.savefig(filename)
        # plt.show()
        # plt.close()

    except Exception as e:
        print(f"Error in plot_neville_interpolation_graph: {e}")
        raise

def plot_cubic_spline_interpolation_graph(x_vals, y_vals, filename="cubic_spline_interpolation.png"):
    """
    Plots and saves a Cubic Spline interpolation graph using the cubic_spline_interpolation function.

    Parameters:
        x_vals (list): x data points.
        y_vals (list): corresponding y values.
        filename (str): name of the image file to save the plot.

    Raises:
        ValueError: if x_vals and y_vals have different lengths.
        Exception: for any general error.
    """
    try:
        if len(x_vals) != len(y_vals):
            raise ValueError("x_vals and y_vals must be the same length.")

        # Generate 300 x values within the range for smooth plotting
        xs = np.linspace(min(x_vals), max(x_vals), 300)
        
        # Calculate interpolated y values for each x in xs
        ys = [cubic_spline_interpolation(x_vals, y_vals, xi) for xi in xs]

        # Create the plot
        plt.figure()
        plt.plot(x_vals, y_vals, 'o', label='Data Points')  # plot original data points as dots
        plt.plot(xs, ys, '-', label='Cubic Spline Interpolation')  # plot interpolated curve
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Cubic Spline Interpolation Graph')
        plt.legend()
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

        # # Save and show the plot
        # plt.savefig(filename)
        # plt.show()
        # plt.close()

    except Exception as e:
        print(f"Error in plot_cubic_spline_interpolation_graph: {e}")
        raise

def plot_bisection_graph(func, a, b, tol=1e-5, filename="bisection_method.png"):
    """
    Plots and saves a graph for the Bisection method showing the function and the root found.

    Parameters:
        func (function): the function for which to find the root.
        a (float): start of interval.
        b (float): end of interval.
        tol (float): tolerance.
        filename (str): name of the image file to save the plot.
    """
    try:
        # Calculate root using Bisection_Method
        root = Bisection_Method(func, a, b, tol)

        # Generate x values for plotting
        xs = np.linspace(a - 1, b + 1, 300)
        ys = [func(xi) for xi in xs]

        # Create the plot
        plt.figure()
        plt.plot(xs, ys, label='Function f(x)')
        plt.axhline(0, color='black', linewidth=0.5)  # x-axis
        plt.plot(root, func(root), 'ro', label=f'Root at x={root:.5f}')  # root point
        plt.xlabel('X')
        plt.ylabel('f(X)')
        plt.title('Bisection Method Root Finding')
        plt.legend()
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

        # # Save and show the plot
        # plt.savefig(filename)
        # plt.show()
        # plt.close()

    except Exception as e:
        print(f"Error in plot_bisection_graph: {e}")
        raise

def plot_newtonraphson_graph(func, dfunc, x0, tol=1e-5, filename="newtonraphson_method.png"):
    """
    Plots and saves a graph for the Newton-Raphson method showing the function and the root found.

    Parameters:
        func (function): the function for which to find the root.
        dfunc (function): derivative of the function.
        x0 (float): initial guess.
        tol (float): tolerance.
        filename (str): name of the image file to save the plot.
    """
    try:
        # Calculate root using Newton-Raphson
        root = Newton_Raphson(func, dfunc, x0, tol)

        # Generate x values for plotting
        xs = np.linspace(x0 - 2, x0 + 2, 300)
        ys = [func(xi) for xi in xs]

        # Create the plot
        plt.figure()
        plt.plot(xs, ys, label='Function f(x)')
        plt.axhline(0, color='black', linewidth=0.5)  # x-axis
        plt.plot(root, func(root), 'ro', label=f'Root at x={root:.5f}')  # root point
        plt.xlabel('X')
        plt.ylabel('f(X)')
        plt.title('Newton-Raphson Method Root Finding')
        plt.legend()
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

        # # Save and show the plot
        # plt.savefig(filename)
        # plt.show()
        # plt.close()

    except Exception as e:
        print(f"Error in plot_newtonraphson_graph: {e}")
        raise

def plot_secant_graph(func, x0, x1, tol=1e-5, filename="secant_method.png"):
    """
    Plots and saves a graph for the Secant method showing the function and the root found.

    Parameters:
        func (function): the function for which to find the root.
        x0 (float): first initial guess.
        x1 (float): second initial guess.
        tol (float): tolerance.
        filename (str): name of the image file to save the plot.
    """
    try:
        # Calculate root using Secant_Method
        root = Secant_Method(func, x0, x1, tol)

        # Generate x values for plotting
        xs = np.linspace(x0 - 2, x1 + 2, 300)
        ys = [func(xi) for xi in xs]

        # Create the plot
        plt.figure()
        plt.plot(xs, ys, label='Function f(x)')
        plt.axhline(0, color='black', linewidth=0.5)  # x-axis
        plt.plot(root, func(root), 'ro', label=f'Root at x={root:.5f}')  # root point
        plt.xlabel('X')
        plt.ylabel('f(X)')
        plt.title('Secant Method Root Finding')
        plt.legend()
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

        # # Save and show the plot
        # plt.savefig(filename)
        # plt.show()
        # plt.close()

    except Exception as e:
        print(f"Error in plot_secant_graph: {e}")
        raise
