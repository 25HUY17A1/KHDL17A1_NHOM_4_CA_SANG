import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def ham_mat_do_xy(x, y):
    return (6/5) * (x + y**2)
# Hàm tính tích phân
def tich_phan(ham, a, b, buoc):
    ket_qua = 0
    x = a
    while x <= b:
        ket_qua += ham(x) * buoc
        x += buoc
    return ket_qua
def tich_phan_ham_mat_do_theo_y(x):
    return tich_phan(lambda y: ham_mat_do_xy(x, y), 0, 1, 0.001)
def tich_phan_ham_mat_do_theo_x(y):
    return tich_phan(lambda x: ham_mat_do_xy(x, y), 0, 1, 0.001)

# Tính hàm mật độ biên
ham_mat_do_bien_x = tich_phan(tich_phan_ham_mat_do_theo_y, 0, 1, 0.001)
ham_mat_do_bien_y = tich_phan(tich_phan_ham_mat_do_theo_x, 0, 1, 0.001)

# Hàm mật độ có điều kiện
def mat_do_co_dk_y_theo_x(x, y):
    return ham_mat_do_xy(x, y) / ham_mat_do_bien_x

def mat_do_co_dk_x_theo_y(x, y):
    return ham_mat_do_xy(x, y) / ham_mat_do_bien_y

# Tính kỳ vọng E(X) and E(Y)
ky_vong_x = tich_phan(lambda x: x * tich_phan_ham_mat_do_theo_y(x), 0, 1, 0.001)
ky_vong_y = tich_phan(lambda y: y * tich_phan_ham_mat_do_theo_x(y), 0, 1, 0.001)

# Tính phương sai V(X) and V(Y)
phuong_sai_x = tich_phan(lambda x: x**2 * tich_phan_ham_mat_do_theo_y(x), 0, 1, 0.001) - ky_vong_x**2
phuong_sai_y = tich_phan(lambda y: y**2 * tich_phan_ham_mat_do_theo_x(y), 0, 1, 0.001) - ky_vong_y**2

# Tính kỳ vọng có điều kiện E(X|Y) and E(Y|X)
ky_vong_co_dk_x_theo_y = tich_phan(lambda y: tich_phan(lambda x: x * mat_do_co_dk_x_theo_y(x, y), 0, 1, 0.001), 0, 1, 0.001)
ky_vong_co_dk_y_theo_x = tich_phan(lambda x: tich_phan(lambda y: y * mat_do_co_dk_y_theo_x(x, y), 0, 1, 0.001), 0, 1, 0.001)

# Tính tích phân của hàm x*y*f_xy(x, y)
def tich_phan_ham_x_y():
    return tich_phan(lambda x: tich_phan(lambda y: x * y * ham_mat_do_xy(x, y), 0, 1, 0.001), 0, 1, 0.001)

tich_phan_xy = tich_phan_ham_x_y()
hiep_phuong_sai = tich_phan_xy - ky_vong_x * ky_vong_y

# Tính hệ số tương quan
he_so_tuong_quan = hiep_phuong_sai / (math.sqrt(phuong_sai_x * phuong_sai_y))

print(f"Hàm mật độ biên fx(x) là : 1.2*x + 0.4      khi 0<=x<=1 ")
print(f"Hàm mật độ biên fy(y) là : 1.2*y**2 + 0.6   khi 0<=y<=1")
print(f"Hàm mật độ có điều kiện f Y|X(y|x) là : (1.2*x + 1.2*y**2)/(1.2*x + 0.4)       khi 0<=x,y<=1")
print(f"Hàm mật độ có điều kiện f X|Y(x|y) là : (1.2*x + 1.2*y**2)/(1.2*y**2 + 0.6)    khi 0<=x,y<=1")
print(f'Kì vọng E(X) là : {ky_vong_x:.2f}')
print(f'Kì vọng E(Y) là : {ky_vong_y:.2f}')
print(f'Phương sai V(X) là :{phuong_sai_x:.2f}')
print(f'Phương sai V(Y) là :{phuong_sai_y:.2f}')
print(f'E(X|y) là : 1.2*y**2/(2.4*y**2 + 1.2) + 1.2/(3.6*y**2 + 1.8)')
print(f'E(Y|x) là : 1.2*x/(2.4*x + 0.8) + 1.2/(4.8*x + 1.6)')
print(f"Hiệp phương sai Cov(X,Y) là : {hiep_phuong_sai :.2f}")
print(f"Hệ số tương quan p(X,Y) là : {he_so_tuong_quan:.3f}")

# Vẽ biểu đồ 3D của hàm mật độ liên hợp f(x, y)
x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
x_grid, y_grid = np.meshgrid(x_values, y_values)
f_values = ham_mat_do_xy(x_grid, y_grid)
plt.figure(figsize=(10, 7))
contour = plt.contourf(x_grid, y_grid, f_values, cmap='viridis')
plt.colorbar(contour)
plt.title('Hàm mật độ liên hợp f(x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Vẽ biểu đồ hàm mật độ biên fx(x)
fx_values = [(6/5) * (x + (1/3)) for x in x_values]
plt.figure(figsize=(10, 5))
plt.plot(x_values, fx_values, label='Hàm mật độ biên f_x(x)')
plt.title('Hàm mật độ biên f_x(x)')
plt.xlabel('x')
plt.ylabel('f_x(x)')
plt.legend()
plt.grid(True)
plt.show()

# Vẽ biểu đồ hàm mật độ biên fy(y)
fy_values = [(6/5) * ((1/2) + y**2) for y in y_values]
plt.figure(figsize=(10, 5))
plt.plot(y_values, fy_values, label='Hàm mật độ biên f_y(y)')
plt.title('Hàm mật độ biên f_y(y)')
plt.xlabel('y')
plt.ylabel('f_y(y)')
plt.legend()
plt.grid(True)
plt.show()

