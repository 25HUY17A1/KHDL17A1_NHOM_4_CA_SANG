import numpy as np
import matplotlib.pyplot as plt

# Bảng phân phối xác suất của X
X_values = [0, 1, 2, 3, 4, 5, 6, '>6']
P_values = [0.2, 0.3, 0.15, 0.1, 0.1, 0.05, 0.05]
p = 1 - sum(P_values)
P_values.append(p)

# 1) Xác định p và tính khả năng công nhân đó mắc từ 3 lỗi trở lên
Xac_suat_3_loi_tro_len = sum(P_values[3:])
print(f" 1) Xác định p: {p:.2f}")
print(f"    Xác suất công nhân mắc từ 3 lỗi trở lên: {Xac_suat_3_loi_tro_len:.2f}")

# 2) Lập bảng phân phối xác suất của Y và tính kỳ vọng, phương sai của Y
Y_values = [10, 3, 3, 0, 0, -2, -2, -4]
P_Y = P_values

Y_xac_suat = {}
for y, p in zip(Y_values, P_Y):
    if y in Y_xac_suat:
        Y_xac_suat[y] += p
    else:
        Y_xac_suat[y] = p

gia_tri_y = list(Y_xac_suat.keys())
xac_suat_y = list(Y_xac_suat.values())


E_Y = np.sum(np.array(gia_tri_y) * np.array(xac_suat_y))

Var_Y = np.sum(((np.array(gia_tri_y) - E_Y) ** 2) * np.array(xac_suat_y))

print(f"2) Bảng phân phối xác suất của Y:")
for y, p in zip(gia_tri_y, xac_suat_y):
    print(f"   Số tiền thưởng/phạt {y}: Xác suất = {p:.2f}")

print(f"   Kỳ vọng của Y: {E_Y:.2f} triệu đồng")
print(f"   Phương sai của Y: {Var_Y:.4f}")

# Vẽ biểu đồ phân phối xác suất của Y
plt.bar(gia_tri_y, xac_suat_y, tick_label=gia_tri_y)
plt.xlabel("Số tiền thưởng/phạt (triệu đồng)")
plt.ylabel("Xác suất")
plt.title("Biểu đồ phân phối xác suất của Y")
plt.grid()
plt.show()
