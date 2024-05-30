joint_prob = [
    [4/15, 1/15, 4/15],
    [1/15, 2/15, 1/15],
    [0, 2/15, 0]
]

# Tính phân phối xác suất biên của X và Y
marginal_X = [sum(row) for row in joint_prob]
marginal_Y = [sum(joint_prob[i][j] for i in range(3)) for j in range(3)]

# Tính kỳ vọng của X và Y
values_X = [-1, 15, 20]
values_Y = [-1, 0, 1]

E_X = sum(marginal_X[i] * values_X[i] for i in range(3))
E_Y = sum(marginal_Y[j] * values_Y[j] for j in range(3))

# Tính kỳ vọng của X*Y
E_XY = sum(values_X[i] * values_Y[j] * joint_prob[i][j] for i in range(3) for j in range(3))

# Tính Cov(X,Y)
cov_XY = E_XY - E_X * E_Y

# Tính phương sai của X và Y
var_X = sum(marginal_X[i] * (values_X[i] - E_X)**2 for i in range(3))
var_Y = sum(marginal_Y[j] * (values_Y[j] - E_Y)**2 for j in range(3))

# Tính hệ số tương quan ρ(X,Y)
import math
corr_XY = cov_XY / math.sqrt(var_X * var_Y)

print("Phân phối xác suất biên của X:", marginal_X)
print("Phân phối xác suất biên của Y:", marginal_Y)
print("Kỳ vọng của X:", E_X)
print("Kỳ vọng của Y:", E_Y)
print("Kỳ vọng của X*Y:", E_XY)
print("Cov(X,Y):", cov_XY)
print("Hệ số tương quan ρ(X,Y):", corr_XY)

