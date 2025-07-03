import os
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from analiza_lib import *
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for your frontend origin if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== Input Models ====================
print("rrrrrrrrrrrrrrr")
class LinearSystemInput(BaseModel):
    coefficients: List[List[float]]
    constants: List[float]
    tolerance: float
    initial_guess: List[float]

class SingleVarEquationInput(BaseModel):
    func: str  # You might parse this with eval; or keep predefined for safety
    derivative: Optional[str] = None
    x0: float
    x1: Optional[float] = None
    tol: float
    max_iter: int

class IntegrationInput(BaseModel):
    func: str
    a: float
    b: float
    n: int  # Number of intervals, or level for Romberg

class InterpolationInput(BaseModel):
    x_vals: List[float]
    y_vals: List[float]
    x: float

# ==================== Iterative Solvers ====================

@app.post("/jacobi")
def run_jacobi(data: LinearSystemInput):
    print("jacobi")
    results = []
    def print_capture(msg):
        results.append(msg)
    import builtins
    original_print = builtins.print
    builtins.print = print_capture

    try:
        jacobi_solver(data.coefficients, data.constants, data.tolerance, data.initial_guess)
    except Exception as e:
        print("error:", e)
        return {"error": str(e)}
    finally:
        builtins.print = original_print

    return {"iterations": results}

@app.post("/gauss_seidel")
def run_gauss_seidel(data: LinearSystemInput):
    print("gauss_seidel")
    results = []
    def print_capture(msg):
        results.append(msg)
    import builtins
    original_print = builtins.print
    builtins.print = print_capture

    try:
        gauss_seidel_solver(data.coefficients, data.constants, data.tolerance, data.initial_guess)
    except Exception as e:
        print("error:", e)
        return {"error": str(e)}
    finally:
        builtins.print = original_print

    return {"iterations": results}

@app.post("/condition_number")
def run_condition_number(matrix: List[List[float]]):
    print("condition_number")
    try:
        mat_np = np.array(matrix)
        cond = condition_number(mat_np)
        return {"condition_number": cond}
    except Exception as e:
        return {"error": str(e)}

# ==================== Root-Finding Methods ====================

@app.post("/newton_raphson")
def run_newton_raphson(data: SingleVarEquationInput):
    print("newton_raphson")
    try:
        f1 = eval("lambda x: " + data.func)
        if data.derivative is None:
            raise ValueError("This method requires a derivative, but none was provided.")
        f2 = eval("lambda x: " + data.derivative)
        plot_b64  = plot_newtonraphson_graph(f1, f2, data.x0)
        result = Newton_Raphson(f1, f2, data.x0, data.tol, data.max_iter)
        return {"result": result, "plot_base64": plot_b64}
    except Exception as e:
        return {"error": str(e)}

@app.post("/bisection")
def run_bisection(data: SingleVarEquationInput):
    try:
        f = eval("lambda x: " + data.func)
        plot_b64  = plot_bisection_graph(f, data.x0, data.x1)
        result = Bisection_Method(f, data.x0, data.x1, data.tol, data.max_iter)
        return {"result": result, "plot_base64": plot_b64}
    except Exception as e:
        return {"error": str(e)}

@app.post("/secant")
def run_secant(data: SingleVarEquationInput):
    try:
        f = eval("lambda x: " + data.func)
        plot_b64  = plot_secant_graph(f, data.x0, data.x1)
        result = Secant_Method(f, data.x0, data.x1, data.tol, data.max_iter)
        return {"result": result, "plot_base64": plot_b64}
    except Exception as e:
        return {"error": str(e)}

# ==================== Numerical Integration ====================

@app.post("/romberg")
def run_romberg(data: IntegrationInput):
    try:
        f = eval("lambda x: " + data.func)
        result = romberg_integration(f, data.a, data.b, data.n)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

@app.post("/simpsons")
def run_simpsons(data: IntegrationInput):
    try:
        f = eval("lambda x: " + data.func)
        result = simpsons_rule(f, data.a, data.b, data.n)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

@app.post("/trapezoidal")
def run_trapezoidal(data: IntegrationInput):
    try:
        f = eval("lambda x: " + data.func)
        result = trapezoidal_rule(f, data.a, data.b, data.n)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

# ==================== Interpolation ====================

@app.post("/linear_interpolation")
def run_linear_interpolation(data: InterpolationInput):
    try:
        plot_b64  = plot_linear_interpolation_graph(data.x_vals, data.y_vals)
        result = linear_interpolation(data.x_vals, data.y_vals, data.x)
        return {"result": result, "plot_base64": plot_b64}
    except Exception as e:
        return {"error": str(e)}

@app.post("/polynomial_interpolation")
def run_polynomial_interpolation(data: InterpolationInput):
    try:
        plot_b64  = plot_polynomial_interpolation_graph(data.x_vals, data.y_vals)
        result = polynomial_interpolation(data.x_vals, data.y_vals, data.x)
        return {"result": result, "plot_base64": plot_b64}
    except Exception as e:
        return {"error": str(e)}

@app.post("/lagrange")
def run_lagrange(data: InterpolationInput):
    try:
        plot_b64  = plot_lagrange_interpolation_graph(data.x_vals, data.y_vals)
        result = lagrange_interpolation(data.x_vals, data.y_vals, data.x)
        return {"result": result, "plot_base64": plot_b64}
    except Exception as e:
        return {"error": str(e)}

@app.post("/neville")
def run_neville(data: InterpolationInput):
    try:
        plot_b64  = plot_neville_interpolation_graph(data.x_vals, data.y_vals)
        result = neville(data.x_vals, data.y_vals, data.x)
        return {"result": result, "plot_base64": plot_b64}
    except Exception as e:
        return {"error": str(e)}

@app.post("/cubic_spline")
def run_cubic_spline(data: InterpolationInput):
    try:
        plot_b64  = plot_cubic_spline_interpolation_graph(data.x_vals, data.y_vals)
        result = cubic_spline_interpolation(data.x_vals, data.y_vals, data.x)
        return {"result": result, "plot_base64": plot_b64}
    except Exception as e:
        return {"error": str(e)}

@app.get("/ping")
def ping():
    print("✅ PING CALLED ✅")
    return {"message": "pong"}
