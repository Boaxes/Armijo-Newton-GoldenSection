import numpy as np

tolerance = 1e-6
alpha_decay = 0.8
armijo_constant = 0.2
x = 4.0

def objective(x):
    return (x - 1)**2 + np.cos(0.5 * x**2)**2

def gradient(x):
    return 2 * (x - 1) - 2 * x * np.cos(0.5 * x**2) * np.sin(0.5 * x**2)

current_value = objective(x)
iteration = 0
print(f"Iteration {iteration}: x = {x}, f(x) = {current_value}")

while abs(gradient(x)) >= tolerance:
    grad = gradient(x)
    direction = -np.sign(grad)
    step_size = 1.0
    previous_value = current_value
    while objective(x + step_size * direction) > previous_value + armijo_constant * step_size * grad * direction:
        step_size *= alpha_decay
    x += step_size * direction
    current_value = objective(x)
    iteration += 1
    print(f"Iteration {iteration}: x = {x}, f(x) = {current_value}")

print(f"Minimum found at x = {x}, f(x) = {current_value}, after {iteration} iterations.")
