import numpy as np
import matplotlib.pyplot as plt

def ham_mat_do_y(y):
    if -1 <= y <= 0:
        return 1 + y
    elif 0 < y <= 1:
        return 1 - y
    else:
        return 0
def tinh_xac_suat(a, b, ham):
    gia_tri_y = np.linspace(a, b, 1000)
    xac_suat = np.trapz([ham(y) for y in gia_tri_y], gia_tri_y)
    return xac_suat
a = -0.25
b = 0.25
xac_suat = tinh_xac_suat(a, b, ham_mat_do_y)

print(f"Xác suất để họ gặp nhau trong khoảng thời gian không quá 15 phút (0.25 giờ) là: {xac_suat:.4f} hay {xac_suat*100:.2f}%")

# Vẽ đồ thị hàm mật độ xác suất của Y
gia_tri_y = np.linspace(-1, 1, 1000)
ham_y = [ham_mat_do_y(y) for y in gia_tri_y]
plt.plot(gia_tri_y, ham_y, label='$f_Y(y)$')
plt.fill_between(gia_tri_y, ham_y, where=(gia_tri_y >= a) & (gia_tri_y <= b), color='skyblue', alpha=0.5, label='|Y| ≤ 0.25')
plt.xlabel('$Y = X_2 - X_1$')
plt.ylabel('$f_Y(y)$')
plt.title('Hàm mật độ xác suất của $Y = X_2 - X_1$')
plt.legend()
plt.grid(True)
plt.show()
