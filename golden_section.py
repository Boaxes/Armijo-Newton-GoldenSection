import math

def f(x):
    return (x - 1)**2 + math.cos(x**2 / 2)**2

def golden_section_search(f, a, b, tol=1e-5):
    gr = (math.sqrt(5) + 1) / 2
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    iteration = 0
    while abs(b - a) > tol:
        print(f"Iteration {iteration}: a = {a:.6f}, b = {b:.6f}")
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gr
        d = a + (b - a) / gr
        iteration += 1
    print(f"Final interval: a = {a:.6f}, b = {b:.6f}")
    return (a + b) / 2

minimizer = golden_section_search(f, a=0, b=3)
print(f"\nEstimated Minimizer: {minimizer}")
print(f"Minimum Value: {f(minimizer)}")
