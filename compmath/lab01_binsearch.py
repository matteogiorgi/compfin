from datetime import datetime


def binary_search(func, a, b, eps=0.00001, max_iterations=1000):
    """
    Binary Search Method for Finding Roots of a Function

    Parameters:
    - func: A function that takes a single argument and returns a value.
    - a: Left endpoint of the interval.
    - b: Right endpoint of the interval.
    - eps: Tolerance for convergence (default: 0.00001).
    - max_iterations: Maximum number of iterations.

    Returns:
    - roots: List of root estimates at each iteration.
    - values: List of function values at each iteration.
    """

    # Check if the function changes sign at the endpoints
    if func(a) > 0:
        # Swap a and b if necessary to ensure a is on the negative side
        a, b = b, a

    if func(a) >= 0 or func(b) <= 0:
        print("Error: Function must have opposite signs at endpoints.")
        return [], []

    roots = []
    values = []
    iteration = 1

    while True:

        c = (a + b) / 2
        roots.append(c)
        f_c = func(c)
        values.append(f_c)

        # Check for convergence or maximum iterations
        if abs(f_c) < eps or iteration == max_iterations:
            break

        # Narrow down the interval based on the sign of func(c)
        if f_c > 0:
            b = c  # Move the right endpoint
        elif f_c < 0:
            a = c  # Move the left endpoint

        iteration += 1

    print(f"Binary search performed {iteration} iterations")
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


fun = lambda x: x**5 - x**3 + 2
a = -1.5
b = -1

start_time = datetime.now()
roots, values = binary_search(fun, a, b)
print("Execution time:", datetime.now() - start_time)

display_results(roots, values)
