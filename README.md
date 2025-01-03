# Numerical Methods for Solving Equations

This repository contains Python implementations of two common numerical methods for finding the roots of equations:

1. **Bisection Method**
2. **Newton-Raphson Method**

Both methods are used to solve nonlinear equations numerically. The code demonstrates the solution of the equation `f(x) = x^2 - 4` as an example.

## Functions

### `bisection_method(func, a, b, tol)`

This function solves the equation `f(x) = 0` using the Bisection Method.

#### Parameters:
- `func (callable)`: The function for which the root is to be found.
- `a (float)`: The lower bound of the interval.
- `b (float)`: The upper bound of the interval.
- `tol (float)`: The tolerance level for the solution.

#### Returns:
- `float`: The root of the function within the specified tolerance.

#### Example:
```python
root_bisection = bisection_method(lambda x: x**2 - 4, 0, 3, 1e-5)
```

### `newton_raphson_method(func, derivative, x0, tol, max_iter)`

This function solves the equation `f(x) = 0` using the Newton-Raphson Method.

#### Parameters:
- `func (callable)`: The function for which the root is to be found.
- `derivative (callable)`: The derivative of the function.
- `x0 (float)`: Initial guess for the root.
- `tol (float)`: The tolerance level for the solution.
- `max_iter (int)`: Maximum number of iterations.

#### Returns:
- `float`: The root of the function within the specified tolerance.

#### Example:
```python
root_newton = newton_raphson_method(lambda x: x**2 - 4, lambda x: 2*x, 3.0, 1e-5, 50)
```

## Example Usage

```python
if __name__ == "__main__":
    print("Numerical Methods for Solving Equations")

    # Example function: f(x) = x^2 - 4
    func = lambda x: x**2 - 4
    derivative = lambda x: 2*x

    # Bisection Method Example
    print("\nUsing Bisection Method:")
    root_bisection = bisection_method(func, 0, 3, 1e-5)
    print(f"Root (Bisection): {root_bisection}\n")

    # Newton-Raphson Method Example
    print("Using Newton-Raphson Method:")
    root_newton = newton_raphson_method(func, derivative, 3.0, 1e-5, 50)
    print(f"Root (Newton-Raphson): {root_newton}")
```

## Requirements

- Python 3.x
- NumPy (for mathematical operations)

To install the required dependencies, you can use pip:

```bash
pip install numpy
```

## Contributing

Feel free to fork the repository, create a branch, and submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License.
```
