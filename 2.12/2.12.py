import math

# Khai báo các biến
n = 20
p = 0.4

# 1. Tính giá trị trung bình
mean = n * p
print(f'Giá trị trung bình E(X): {mean:.2f}')

# 2. Tính độ lệch chuẩn
std_dev = math.sqrt(n * p * (1 - p))
print(f'Độ lệch chuẩn σ: {std_dev:.2f}')

# 3. Tính Mode
mode = math.floor((n + 1) * p)
print(f'Mode của X: {mode}')

# 4. Tính P(X = 10)
k = 10
q = 1 - p
P_X_equals_10 = math.comb(n, k) * (p ** k) * (q ** (n - k))
print(f'P(X = 10): {P_X_equals_10:.6f}')
