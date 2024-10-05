from scipy.optimize import approx_fprime
from datetime import datetime


def newtons_method_root(func, x_0, eps=0.00001, max_iterations=100):
    """
    Newton's Method for Finding Roots of a Function using Numerical Derivatives

    Parameters:
    - func: A Python function representing the function.
    - x_0: Initial guess for the root.
    - eps: Tolerance for convergence (default: 0.00001).
    - max_iterations: Maximum number of iterations (default: 100).

    Returns:
    - roots: List of root estimates at each iteration.
    - values: List of function values at each iteration.
    """

    # Initialize root estimate and values
    roots = [x_0]
    values = [func(x_0)]
    iteration = 1

    while True:
        # Compute the numerical derivative
        df = approx_fprime(roots[-1], lambda x: func(x), eps)[0]

        # Check if the derivative is not zero
        if df != 0:
            # Newton's method formula: x_(n+1) = x_n - f(x_n) / f'(x_n)
            x_estimate = roots[-1] - func(roots[-1]) / df
            roots.append(x_estimate)
            values.append(func(x_estimate))
        else:
            break

        # Stop if max iterations reached or convergence criteria met
        if abs(values[-1]) < eps or iteration >= max_iterations:
            break

        iteration += 1

    print(f"Newton Method performed {iteration} iterations")
    return roots, values


def display_results(roots, values):
    if not roots:
        print("No results to display.")
        return

    num_iterations = len(roots)

    # Print table header
    print(f"{'Iteration':<12}{'Root Estimate':<20}{'Function Value':<20}")
    print("=" * 56)

    for i in range(num_iterations):
        print(f"{i + 1:<12}{roots[i]:<20.6f}{values[i]:<20.6f}")


def f(x):
    return x ** 5 - x ** 3 + 2


# Initial guess
x0 = -1.5

start_time = datetime.now()
newton_roots, newton_values = newtons_method_root(f, x0)
print("Execution time:", datetime.now() - start_time)

display_results(newton_roots, newton_values)
