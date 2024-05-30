# Tính hệ số c
def calculate_c():
    total_sum = 0
    x = 0
    while True:
        term = (1 / 3) ** x
        total_sum += term
        if term < 1e-6:  # Điều kiện dừng (đủ gần 0)
            break
        x += 1
    return 1 / total_sum

# Tính giá trị kỳ vọng E(X)
def calculate_expected_value():
    c = calculate_c()
    expected_value = 0
    x = 0
    while True:
        term = x * c * (1 / 3) ** x
        expected_value += term
        if term < 1e-6:  # Điều kiện dừng (đủ gần 0)
            break
        x += 1
    return expected_value

# Tính xác suất P(X ≥ 3)
def calculate_probability_ge_3():
    c = calculate_c()
    probability_ge_3 = 0
    for x in range(3, 100):  # Giả sử x không vượt quá 100
        term = c * (1 / 3) ** x
        probability_ge_3 += term
    return probability_ge_3

# Tính xác suất P(X = 2k + 1) với k là số nguyên không âm
def calculate_probability_odd_k(k):
    if k >= 0:
        c = calculate_c()
        return c * (1 / 3) ** (2 * k + 1)
    else:
        return 0

# Gọi các hàm để tính giá trị
c_value = calculate_c()
expected_value = calculate_expected_value()
probability_ge_3 = calculate_probability_ge_3()
probability_odd_k_1 = calculate_probability_odd_k(1)

print(f"Hệ số c: {c_value}")
print(f"Giá trị kỳ vọng E(X): {expected_value}")
print(f"Xác suất P(X ≥ 3): {probability_ge_3}")
print(f"Xác suất P(X = 3): {probability_odd_k_1}")
