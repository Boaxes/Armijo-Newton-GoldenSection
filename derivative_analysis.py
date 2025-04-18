from sympy import symbols, cos, pi, diff, simplify, solve

x = symbols('x')
f = (x - 1)**2 + cos(pi * x / 2)**2
f_prime = diff(f, x)
f_prime_simplified = simplify(f_prime)
critical_points = solve(f_prime_simplified, x)
f_prime_simplified, critical_points
