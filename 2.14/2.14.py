import math
# Khai báo biến
x = 10
delta_x = 1

# Định nghĩa hàm f(x)
def f_x(x):
    return 1 / 20

# Tính tổng Riemann
integral_sum = 0
while x <= 20:
    integral_sum += f_x(x) * delta_x
    x += delta_x

print(f'Tích phân của f(x) từ 10 đến 20: {integral_sum:.6f}')

# Kiểm tra nếu tổng Riemann bằng 1
if math.isclose(integral_sum, 1):
    print('f(x) là hàm mật độ xác suất.')
else:
    print('f(x) không phải là hàm mật độ xác suất.')
