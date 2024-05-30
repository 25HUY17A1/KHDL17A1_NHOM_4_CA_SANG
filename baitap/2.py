# Tính kỳ vọng của X
E_X = integrate.quad(lambda x: 3*x**3, 0, 1)[0]

# Tính kỳ vọng của X^2
E_X_square = integrate.quad(lambda x: 3*x**4, 0, 1)[0]

# Tính phương sai của X
Var_X = E_X_square - E_X**2

# Tính trung vị của X
median_X = 0.5

# Tính hệ số bất đối xứng của X
skewness_X = 0

# Tính hệ số nhọn của X
kurtosis_X = 6 / 5

print("Kỳ vọng của X:", E_X)
print("Phương sai của X:", Var_X)
print("Trung vị của X:", median_X)
print("Hệ số bất đối xứng của X:", skewness_X)
print("Hệ số nhọn của X:", kurtosis_X)
