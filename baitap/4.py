import sympy as sp

# Khai báo biến
x = sp.symbols('x')

# Định nghĩa hàm mật độ xác suất
a = sp.symbols('a', real=True, positive=True)
f_x1 = a * x**2
f_x2 = a * (2 - x)**2

# 1. Tìm giá trị của a
integral_f_x1 = sp.integrate(f_x1, (x, 0, 1))
integral_f_x2 = sp.integrate(f_x2, (x, 1, 2))
eq = integral_f_x1 + integral_f_x2 - 1
a_value = sp.solve(eq, a)[0]

# Thay giá trị của a vào các hàm mật độ
f_x1 = f_x1.subs(a, a_value)
f_x2 = f_x2.subs(a, a_value)

# 2. Tìm kỳ vọng E[X]
E_X = sp.integrate(x * f_x1, (x, 0, 1)) + sp.integrate(x * f_x2, (x, 1, 2))

# Tìm E[X^2]
E_X2 = sp.integrate(x**2 * f_x1, (x, 0, 1)) + sp.integrate(x**2 * f_x2, (x, 1, 2))

# Tìm phương sai Var(X)
Var_X = E_X2 - E_X**2

# Tìm độ lệch chuẩn sigma_X
sigma_X = sp.sqrt(Var_X)

# 3. Tính P(0.5 < X < 2)
P_0_5_to_2 = sp.integrate(f_x1, (x, 0.5, 1)) + sp.integrate(f_x2, (x, 1, 2))

# In kết quả
a_value.evalf(), E_X.evalf(), Var_X.evalf(), sigma_X.evalf(), P_0_5_to_2.evalf()
