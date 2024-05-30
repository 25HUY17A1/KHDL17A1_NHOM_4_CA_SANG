import numpy as np

# Định nghĩa hàm mật độ xác suất f(x)
def f(x):
    if 1 <= x <= 4:
        return (x - 1) / 3
    else:
        return 0

# Tính tích phân bằng phương pháp hình chữ nhật
def integrate(f, a, b, n=10000):
    x = np.linspace(a, b, n)
    y = np.array([f(xi) for xi in x])
    dx = (b - a) / n
    return np.sum(y * dx)

# Tính kỳ vọng E[X]
def integrand_expectation(x):
    return x * f(x)

E_X = integrate(integrand_expectation, 1, 4)

# Tính E[X^2]
def integrand_expectation_squared(x):
    return x**2 * f(x)

E_X2 = integrate(integrand_expectation_squared, 1, 4)

# Tính phương sai Var(X)
Var_X = E_X2 - E_X**2

# Tìm mốt của X
mode_X = 4  # Vì hàm mật độ xác suất tăng dần từ 1 đến 4 và đạt giá trị lớn nhất tại x = 4

# In kết quả
print(f"Kỳ vọng E[X]: {E_X}")
print(f"Phương sai Var(X): {Var_X}")
print(f"Mốt của X: {mode_X}")
