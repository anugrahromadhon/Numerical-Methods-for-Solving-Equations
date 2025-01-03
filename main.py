import numpy as np

def bisection_method(func, a, b, tol):
    """
    Solve a function using the Bisection Method.

    Parameters:
    func (callable): The function to solve.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    tol (float): The tolerance level for the solution.

    Returns:
    float: The root of the function within the tolerance.
    """
    if func(a) * func(b) > 0:
        raise ValueError("The function must have opposite signs at the interval endpoints.")

    iteration = 0
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

        iteration += 1
        print(f"Iteration {iteration}: Interval = [{a}, {b}], Midpoint = {midpoint}, f(Midpoint) = {func(midpoint)}")

    return (a + b) / 2

def newton_raphson_method(func, derivative, x0, tol, max_iter):
    """
    Solve a function using the Newton-Raphson Method.

    Parameters:
    func (callable): The function to solve.
    derivative (callable): The derivative of the function.
    x0 (float): Initial guess.
    tol (float): Tolerance level for the solution.
    max_iter (int): Maximum number of iterations.

    Returns:
    float: The root of the function within the tolerance.
    """
    x = x0
    for i in range(max_iter):
        fx = func(x)
        dfx = derivative(x)

        if dfx == 0:
            raise ValueError("Derivative is zero. Newton-Raphson method fails.")

        x_new = x - fx / dfx
        print(f"Iteration {i + 1}: x = {x}, f(x) = {fx}, Derivative = {dfx}, New x = {x_new}")

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    raise ValueError("Maximum iterations reached without convergence.")

def parse_function(input_str):
    """
    Parse a mathematical function string into a callable function.

    Parameters:
    input_str (str): The mathematical function as a string.

    Returns:
    callable: The parsed function.
    """
    return lambda x: eval(input_str)

if __name__ == "__main__":
    print("Numerical Methods for Solving Equations")

    # User inputs the function
    func_str = input("Enter the function f(x) (e.g., x**2 - 4): ")
    func = parse_function(func_str)

    # User inputs the derivative for Newton-Raphson method
    derivative_str = input("Enter the derivative f'(x) (e.g., 2*x): ")
    derivative = parse_function(derivative_str)

    # User inputs the method to use
    method = input("Choose a method (bisection/newton): ").strip().lower()

    if method == "bisection":
        a = float(input("Enter the lower bound (a): "))
        b = float(input("Enter the upper bound (b): "))
        tol = float(input("Enter the tolerance: "))

        try:
            root_bisection = bisection_method(func, a, b, tol)
            print(f"Root (Bisection): {root_bisection}")
        except ValueError as e:
            print(e)

    elif method == "newton":
        x0 = float(input("Enter the initial guess (x0): "))
        tol = float(input("Enter the tolerance: "))
        max_iter = int(input("Enter the maximum number of iterations: "))

        try:
            root_newton = newton_raphson_method(func, derivative, x0, tol, max_iter)
            print(f"Root (Newton-Raphson): {root_newton}")
        except ValueError as e:
            print(e)

    else:
        print("Invalid method. Please choose either 'bisection' or 'newton'.")
