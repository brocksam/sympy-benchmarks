"""Benchmarks for optimizing float point expressions for numerical accuracy.

The benchmark cases are based on the 28 examples in the FPBench/FPBench
repository. These in turn are adapted from Chapter 3 of Hamming, R. (2012).
Numerical methods for scientists and engineers. Courier Corporation.

"""

from sympy import atan, cos, sin, sqrt


# Problem 1
def test_hamming_nmse_problem_3_1(x):
    """Algebraic rearrangement example using a numerator rationalization method.

    For large x this should be replaced by:

    1 / (sqrt(x + 1) + sqrt(x))

    """
    assert x >= 0
    y = sqrt(x + 1) - sqrt(x)


# Problem 2
def test_hamming_nmse_problem_3_3(x, eps):
    """Algebraic rearrangement example using a trigonometric identity method.

    For small eps this should be replaced by:

    2 * cos(x + (eps / 2)) * sin(eps / 2)

    """
    y = sin(x + eps) - sin(x)


# Problem 3
def test_hamming_nmse_problem_3_4(x):
    """Algebraic rearrangement example using a trigonometric identity method.

    For small x this should be replaced by:

    tan(x / 2)

    """
    assert x != 0
    y = (1 - cos(x)) / sin(x)


# Problem 4
def test_hamming_nmse_problem_3_5(N):
    """Algebraic rearrangement example using a trigonometric identity method.

    For large N this should be replaced by:

    atan(1 / (1 + N * (N + 1)))

    """
    y = atan(N + 1) - atan(N)


# Problem 5
def test_hamming_nmse_problem_3_6(x):
    """Algebraic rearrangement example using a common denominator method.

    For large x this should be replaced by:

    1 / ((x + 1) * sqrt(x) + x * sqrt(x + 1))

    """
    assert x >= 0
    y = (1 / sqrt(x)) - (1 / sqrt(x + 1))


# Problem 6
def test_hamming_nmse_problem_3_3_1(x):
    """Algebraic rearrangement example using a common denominator method.

    For large x this should be replaced by:

    1 / (x * (x + 1))

    """
    assert x != 0
    y = (1 / (x + 1)) - (1 / x)


# Problem 7
def test_hamming_nmse_problem_3_3_2(x, eps):
    """Algebraic rearrangement example using a trigonometric identity method.

    For small eps this should be replaced by:

    sin(eps) / (cos(x) * cos(x + eps))

    """
    y = tan(x + eps) - tan(x)


# Problem 8
def test_hamming_nmse_problem_3_3_3(x):
    """Algebraic rearrangement example using a common denominator method.

    For large x this should be replaced by:

    2 / (x * (x**2 - 1))

    """
    assert (x != -1) or (x != 0) or (x != 1)
    y = (1 / (x + 1)) - (2 / x) + (1 / (x - 1))


# Problem 9
def test_hamming_nmse_problem_3_3_4(x):
    """Algebraic rearrangement example.

    TODO: find method expected replacement using Herbie.

    """
    assert x >= 0
    y = (x + 1)**(1 / 3) - x**(1 / 3)


# Problem 10
def test_hamming_nmse_problem_3_3_5(x, eps):
    """Algebraic rearrangement example.
    
    TODO: find method and expected replacement using Herbie.

    """
    assert x >= 0
    y = cos(x + eps) - cos(x)


# Problem 11
def test_hamming_nmse_problem_3_3_6(N):
    """Algebraic rearrangement example.

    TODO: find method and expected replacement using Herbie.

    """
    assert N > 0
    y = log(N + 1) - log(N)


# Problem 12
def test_hamming_nmse_problem_3_3_7(x):
    """Algebraic rearrangement example using a trigonometric identity method.

    For small eps this should be replace by:

    4 * sinh(eps / 2)**2

    """
    y = exp(eps) - 2 + exp(-eps)


# Problem 13
def test_hamming_nmse_p42_positive(a, b, c):
    """Quadratic formula example.

    TODO: find method and expected replacement using Herbie.

    """
    assert (b * b >= 4 * a * c) and (a != 0)
    y = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)


# Problem 14
def test_hamming_nmse_p42_negative(a, b, c):
    """Quadratic formula example.

    TODO: find method and expected replacement using Herbie.

    """
    assert (b * b >= 4 * a * c) and (a != 0)
    y = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)


# Problem 15
def test_hamming_nmse_problem_3_2_1_positive(a, b2, c):
    """Quadratic formula example.

    TODO: find method and expected replacement using Herbie.

    """
    assert (b2 * b2 >= a * c) and (a != 0)
    y = (-b2 + sqrt(b2 * b2 - a * c)) / a


# Problem 16
def test_hamming_nmse_problem_3_2_1_negative(a, b2, c):
    """Quadratic formula example.

    TODO: find method and expected replacement using Herbie.

    """
    assert (b2 * b2 >= a * c) and (a != 0)
    y = (-b2 - sqrt(b2 * b2 - a * c)) / a


# Problem 17
def test_hamming_nmse_problem_3_7(x):
    """Series expansion example.

    For small x this should be replaced by:

    x * (1 + (x / 2) + (x**2 / 6) + ...)

    """
    y = exp(x) - 1


# Problem 18
def test_hamming_nmse_problem_3_8(N):
    """Series expansion example.

    For small N this should be replaced by:

    log(N + 1) - (1 / (2 * N)) + (1 / (3 * N**2)) - (1 / (4 * N**3)) + ...

    """
    assert N > 0
    y = (N + 1) * log(N + 1) - N * log(N) - 1


# Example 19
def test_hamming_nmse_problem_3_9(x):
    """Series expansion example.

    For small x this should be replaced by:

    (x / 3) * (1 + (x**2 / 15) + ...)

    """
    assert x != 0
    y = (1 / x) - (1 / tan(x))


# Example 20
def test_hamming_nmse_problem_3_10(x):
    """Series expansion example.

    For small x this should be replaced by:

    - (1 + x + (x**2 / 2) + (5 * x**3 / 12) + ...)

    """
    assert -1 < x < 1
    y = log(1 - x) / log(1 + x)


# Example 21
def test_hamming_nmse_problem_3_4_1(eps):
    """Series expansion example.

    TODO: find expected replacement using Herbie.

    """
    assert eps != 0
    y = (1 - cos(eps)) / eps**2


# Example 22
def test_hamming_nmse_problem_3_4_2(a, b, eps):
    """Series expansion example.

    For small eps this should be replaced by:

    (a + b) / (a * b)

    """
    assert eps != 0
    y = (eps * (exp((a + b) * eps)) - 1) / ((exp(a * eps) - 1) * (exp(b * eps) - 1))


# Example 23
def test_hamming_nmse_problem_3_4_3(eps):
    """Series expansion example.

    For small eps this should be replaced by:

    -2 * (eps + (eps**3 / 3) + (eps**5 / 5) + ...)
    """
    assert -1 < eps < 1
    y = log((1 - eps) / (1 + eps))


# Example 24
def test_hamming_nmse_problem_3_4_4(eps):
    """Series expansion example.

    TODO: find expected replacement using Herbie.

    """
    assert eps != 0
    y = sqrt((exp(2 * eps) - 1)) / (exp(eps) - 1)


# Example 25
def test_hamming_nmse_problem_3_4_5(eps):
    """Series expansion example.

    TODO: find expected replacement using Herbie.

    """
    assert eps != 0
    y = (eps - sin(eps)) / (eps - tan(eps))


# Example 26
def test_hamming_nmse_problem_3_4_6(x, n):
    """Series expansion example.

    TODO: find expected replacement using Herbie.

    """
    assert x >= 0
    y = (x + 1)**(1 / n) - x**(1 / n)


# Example 27
def test_hamming_nmse_p49(a, x):
    """Branches and regimes example.

    TODO: find expected replacement using Herbie.

    """
    y = exp(a * x) - 1


# Example 28
def test_hamming_nmse_p58(x):
    """Branches and regimes example.

    TODO: find expected replacement using Herbie.

    """
    assert x != 0
    y = exp(x) / (exp(x) - 1)
