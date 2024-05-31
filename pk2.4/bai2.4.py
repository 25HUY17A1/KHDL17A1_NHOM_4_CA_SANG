import numpy as np
import matplotlib.pyplot as plt

# Xác suất bắn trúng các vòng và bắn trượt
p_vong1 = 0.6
p_vong2 = 0.3
p_truot = 0.1

X_values = [0, 5, 10, 15, 20]
P_X = np.zeros(5)

# Tính xác suất cho từng giá trị của X
P_X[0] = p_truot * p_truot
P_X[1] = p_truot * p_vong2 + p_vong2 * p_truot
P_X[2] = p_truot * p_vong1 + p_vong1 * p_truot + p_vong2 * p_vong2
P_X[3] = p_vong2 * p_vong1 + p_vong1 * p_vong2
P_X[4] = p_vong1 * p_vong1

# Hiển thị bảng phân phối xác suất của X
print("1) Bảng phân phối xác suất của X là:")
for value, change in zip(X_values, P_X):
    print(f"Tổng số điểm {value}: Xác suất = {change:.2f}")

# Vẽ biểu đồ phân phối xác suất của X
plt.bar(X_values, P_X, tick_label=X_values)
plt.xlabel("Tổng số điểm")
plt.ylabel("Xác suất")
plt.title("Biểu đồ phân phối xác suất của X")
plt.grid()
plt.show()

# 2) Tính kỳ vọng, phương sai và Mốt của X
E_X = np.sum(np.array(X_values) * P_X)
Var_X = np.sum((np.array(X_values) - E_X) ** 2 * P_X)
Mode_X = X_values[np.argmax(P_X)]

print(f"2) Kỳ vọng của X là: {E_X:.2f}")
print(f"   Phương sai của X là: {Var_X:.2f}")
print(f"   Mốt của X là: {Mode_X}")