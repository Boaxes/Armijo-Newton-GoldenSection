# Math410HW2.py
import numpy as np
import sympy as sp

x = sp.Symbol('x')
f = (x - 1)**2 + sp.cos(x**2 / 2)**2
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)

f_lambd = sp.lambdify(x, f, modules='numpy')
f_prime_lambd = sp.lambdify(x, f_prime, modules='numpy')
f_double_prime_lambd = sp.lambdify(x, f_double_prime, modules='numpy')

def newtons_method(f_prime, f_double_prime, x0, tol=1e-8, max_iter=20):
    x_n = x0
    results = []
    for i in range(max_iter):
        f_prime_val = f_prime(x_n)
        f_double_prime_val = f_double_prime(x_n)
        if abs(f_double_prime_val) < 1e-10:
            break
        x_next = x_n - f_prime_val / f_double_prime_val
        results.append((i, x_n, f_lambd(x_n)))
        if abs(x_next - x_n) < tol:
            results.append((i+1, x_next, f_lambd(x_next)))
            break
        x_n = x_next
    return results

initial_guess = 2.0
results = newtons_method(f_prime_lambd, f_double_prime_lambd, initial_guess)

for iteration, x_val, f_val in results:
    print(f"Iteration {iteration}: x = {x_val:.6f}, f(x) = {f_val:.6f}")
