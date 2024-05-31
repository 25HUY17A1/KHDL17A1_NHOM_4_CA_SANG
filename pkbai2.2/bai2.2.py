import numpy as np
import matplotlib.pyplot as plt
import math

# Hàm xác suất người thứ nhất bắn trúng x viên
def P1():
    X = []
    p = 0.7
    for i in range(0, 3):
        temp = math.comb(2, i) * (p ** i) * ((1 - p) ** (2 - i))
        X.append(temp)
    return X

# Hàm xác suất người thứ hai bắn trúng x viên
def P2():
    X = []
    p = 0.8
    for i in range(0, 3):
        temp = math.comb(2, i) * (p ** i) * ((1 - p) ** (2 - i))
        X.append(temp)
    return X

# Lấy bảng phân phối xác suất của từng người
X1 = P1()
X2 = P2()

# Tính bảng phân phối xác suất của X, tổng số viên đạn bắn trúng từ cả hai người
P_X = np.zeros(5)
for i in range(3):
    for j in range(3):
        P_X[i+j] += X1[i] * X2[j]

# Hiển thị bảng phân phối xác suất
So_vien_dan_thu_bi_trung = ["0", "1", "2", "3", "4"]
print("1) Bảng phân phối xác suất của X là:")
for i, p in enumerate(P_X):
    print(f"Số viên đạn trúng {i}: Xác suất = {p}")

# Vẽ biểu đồ phân phối xác suất
plt.bar(So_vien_dan_thu_bi_trung, P_X)
plt.xlabel("Số viên đạn trúng")
plt.ylabel("Xác suất")
plt.title("Biểu đồ phân phối xác suất của X")
plt.grid()
plt.show()

# 2) Tính xác suất để số viên đạn trúng thú của hai người bằng nhau
Xac_xuat_bang_nhau = X1[0] * X2[0] + X1[1] * X2[1] + X1[2] * X2[2]
print('2) Xác suất để số viên đạn trúng thú của hai người bằng nhau là:', Xac_xuat_bang_nhau)

# Vẽ biểu đồ cho xác suất để số viên đạn trúng thú của hai người bằng nhau
labels = ["Bằng nhau", "Không bằng nhau"]
values = [Xac_xuat_bang_nhau, 1 - Xac_xuat_bang_nhau]

plt.bar(labels, values, color=['blue', 'orange'])
plt.xlabel("Tình huống")
plt.ylabel("Xác suất")
plt.title("Xác suất số viên đạn trúng thú của hai người bằng nhau")
plt.grid()
plt.show()