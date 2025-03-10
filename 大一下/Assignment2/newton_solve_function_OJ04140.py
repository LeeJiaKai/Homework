def f(x):
    return x**3-5*x**2+10*x-80
def f1(x):
    return 3*x**2-10*x+10

def newton_raphson(f, f1, x0, tol=1e-9, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = f1(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Exceeded maximum iterations. No solution found.")

x0 = 5.0
root = newton_raphson(f, f1, x0)

print(f"{root:.9f}")