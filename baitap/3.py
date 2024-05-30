# Hàm mật độ xác suất của biến ngẫu nhiên X
def f(x):
    if 0 <= x <= 1:
        return 3 * x**2
    else:
        return 0

# Tính kì vọng của biến ngẫu nhiên X
def expected_value():
    E = 0
    for x in range(0, 101):  # Range từ 0 đến 1 với bước nhỏ nhất là 0.01
        E += f(x/100) * (x/100)
    return E

# Tính phương sai của biến ngẫu nhiên X
def variance():
    E_X2 = 0
    E_X = expected_value()
    for x in range(0, 101):
        E_X2 += f(x/100) * (x/100)**2
    return E_X2 - E_X**2

# Tìm trung vị của biến ngẫu nhiên X
def median():
    cumulative_probability = 0
    median_value = None
    for x in range(0, 101):
        cumulative_probability += f(x/100)
        if cumulative_probability >= 0.5:
            median_value = x/100
            break
    return median_value

# Tính hệ số bất đối xứng của biến ngẫu nhiên X
def skewness():
    E_X = expected_value()
    var_X = variance()
    skew = 0
    if var_X != 0:
        for x in range(0, 101):
            skew += f(x/100) * ((x/100 - E_X) / (var_X ** 0.5)) ** 3
    return skew

# Tính hệ số nhọn của biến ngẫu nhiên X
def kurtosis():
    E_X = expected_value()
    var_X = variance()
    kurt = 0
    if var_X != 0:
        for x in range(0, 101):
            kurt += f(x/100) * ((x/100 - E_X) / (var_X ** 0.5)) ** 4
    return kurt

# In kết quả
print("Kì vọng của X:", expected_value())
print("Phương sai của X:", variance())
print("Trung vị của X:", median())
print("Hệ số bất đối xứng của X:", skewness())
print("Hệ số nhọn của X:", kurtosis())
