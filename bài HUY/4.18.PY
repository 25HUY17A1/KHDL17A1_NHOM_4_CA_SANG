import numpy as np

def ham_mat_do_xyz(x, y, z, c):
    return c * (x + y + z)
def tich_phan(ham, a, b, buoc):
    ket_qua = 0
    x = a
    while x < b:
        ket_qua += ham(x) * buoc
        x += buoc
    return ket_qua
# Hàm tính tích phân bội 3 theo phương pháp hình thang
def tich_phan_boi_3(ham, x_a, x_b, y_a, y_b, z_a, z_b, buoc):
    def tich_phan_theo_yz(x):
        return tich_phan(lambda y: tich_phan(lambda z: ham(x, y, z), z_a, z_b, buoc), y_a, y_b, buoc)
    return tich_phan(tich_phan_theo_yz, x_a, x_b, buoc)
# Tính giá trị tham số c
def tim_c():
    c = 1
    ket_qua_tich_phan = tich_phan_boi_3(lambda x, y, z: ham_mat_do_xyz(x, y, z, c), 0, 1, 0, 1, 0, 1, 0.01)
    return 1 / ket_qua_tich_phan
c_gia_tri = tim_c()
print(f"Giá trị của tham số c là: {c_gia_tri:.2f}")

print('Hàm phân phối xác suất là :')
def F_xyz_expression(x_case, y_case, z_case):
    c = 0,67

    if x_case == "x <= 0" and y_case == "y <= 0" and z_case == "z <= 0":
        result = "0"
    elif x_case == "x <= 0" and y_case == "y <= 0" and z_case == "0 <= z <= 1":
        result = f"{c} * (z**2 / 2)"
    elif x_case == "x <= 0" and y_case == "y <= 0" and z_case == "z > 1":
        result = f"{c} * (1 / 2)"
    elif x_case == "x <= 0" and y_case == "0 <= y <= 1" and z_case == "z <= 0":
        result = f"{c} * (y**2 / 2)"
    elif x_case == "x <= 0" and y_case == "0 <= y <= 1" and z_case == "0 <= z <= 1":
        result = f"{c} * (y * z + y**2 / 2 + z**2 / 2)"
    elif x_case == "x <= 0" and y_case == "0 <= y <= 1" and z_case == "z > 1":
        result = f"{c} * (y + y**2 / 2)"
    elif x_case == "x <= 0" and y_case == "y > 1" and z_case == "z <= 0":
        result = f"{c} * (1 / 2)"
    elif x_case == "x <= 0" and y_case == "y > 1" and z_case == "0 <= z <= 1":
        result = f"{c} * (1 / 2 + z)"
    elif x_case == "x <= 0" and y_case == "y > 1" and z_case == "z > 1":
        result = f"{c} * 1"
    elif x_case == "0 <= x <= 1" and y_case == "y <= 0" and z_case == "z <= 0":
        result = f"{c} * (x**2 / 2)"
    elif x_case == "0 <= x <= 1" and y_case == "y <= 0" and z_case == "0 <= z <= 1":
        result = f"{c} * (x * z + x**2 / 2 + z**2 / 2)"
    elif x_case == "0 <= x <= 1" and y_case == "y <= 0" and z_case == "z > 1":
        result = f"{c} * (x + x**2 / 2)"
    elif x_case == "0 <= x <= 1" and y_case == "0 <= y <= 1" and z_case == "z <= 0":
        result = f"{c} * (x * y + x**2 / 2 + y**2 / 2)"
    elif x_case == "0 <= x <= 1" and y_case == "0 <= y <= 1" and z_case == "0 <= z <= 1":
        result = f"{c} * (x * y * z + (x * y**2) / 2 + (x * z**2) / 2 + (y * z**2) / 2 + (y**2 * z) / 2 + (x**2 * y) / 2 + (x**2 * z) / 2 + z**3 / 6 + y**3 / 6 + x**3 / 6)"
    elif x_case == "0 <= x <= 1" and y_case == "0 <= y <= 1" and z_case == "z > 1":
        result = f"{c} * (x * y + x * y**2 / 2 + y**2 / 2 + x * y + y + y**2 / 2 + x**2 / 2 + x)"
    elif x_case == "0 <= x <= 1" and y_case == "y > 1" and z_case == "z <= 0":
        result = f"{c} * (x + x**2 / 2)"
    elif x_case == "0 <= x <= 1" and y_case == "y > 1" and z_case == "0 <= z <= 1":
        result = f"{c} * (x * z + x + x * z + z**2 / 2 + x**2 / 2 + z)"
    elif x_case == "0 <= x <= 1" and y_case == "y > 1" and z_case == "z > 1":
        result = f"{c} * (x + x**2 / 2 + z + z**2 / 2)"
    elif x_case == "x > 1" and y_case == "y <= 0" and z_case == "z <= 0":
        result = f"{c} * (1 / 2)"
    elif x_case == "x > 1" and y_case == "y <= 0" and z_case == "0 <= z <= 1":
        result = f"{c} * (1 / 2 + z)"
    elif x_case == "x > 1" and y_case == "y <= 0" and z_case == "z > 1":
        result = "1"
    elif x_case == "x > 1" and y_case == "0 <= y <= 1" and z_case == "z <= 0":
        result = f"{c} * (y + y**2 / 2)"
    elif x_case == "x > 1" and y_case == "0 <= y <= 1" and z_case == "0 <= z <= 1":
        result = f"{c} * (y + y * z + y**2 / 2 + z**2 / 2)"
    elif x_case == "x > 1" and y_case == "0 <= y <= 1" and z_case == "z > 1":
        result = "1"
    elif x_case == "x > 1" and y_case == "y > 1" and z_case == "z <= 0":
        result = "1"
    elif x_case == "x > 1" and y_case == "y > 1" and z_case == "0 <= z <= 1":
        result = "1"
    elif x_case == "x > 1" and y_case == "y > 1" and z_case == "z > 1":
        result = "1"

    return result

# In ra màn hình tất cả các trường hợp tổng quát
cases = [
    ("x <= 0", "y <= 0", "z <= 0"),
    ("x <= 0", "y <= 0", "0 <= z <= 1"),
    ("x <= 0", "y <= 0", "z > 1"),
    ("x <= 0", "0 <= y <= 1", "z <= 0"),
    ("x <= 0", "0 <= y <= 1", "0 <= z <= 1"),
    ("x <= 0", "0 <= y <= 1", "z > 1"),
    ("x <= 0", "y > 1", "z <= 0"),
    ("x <= 0", "y > 1", "0 <= z <= 1"),
    ("x <= 0", "y > 1", "z > 1"),
    ("0 <= x <= 1", "y <= 0", "z <= 0"),
    ("0 <= x <= 1", "y <= 0", "0 <= z <= 1"),
    ("0 <= x <= 1", "y <= 0", "z > 1"),
    ("0 <= x <= 1", "0 <= y <= 1", "z <= 0"),
    ("0 <= x <= 1", "0 <= y <= 1", "0 <= z <= 1"),
    ("0 <= x <= 1", "0 <= y <= 1", "z > 1"),
    ("0 <= x <= 1", "y > 1", "z <= 0"),
    ("0 <= x <= 1", "y > 1", "0 <= z <= 1"),
    ("0 <= x <= 1", "y > 1", "z > 1"),
    ("x > 1", "y <= 0", "z <= 0"),
    ("x > 1", "y <= 0", "0 <= z <= 1"),
    ("x > 1", "y <= 0", "z > 1"),
    ("x > 1", "0 <= y <= 1", "z <= 0"),
    ("x > 1", "0 <= y <= 1", "0 <= z <= 1"),
    ("x > 1", "0 <= y <= 1", "z > 1"),
    ("x > 1", "y > 1", "z <= 0"),
    ("x > 1", "y > 1", "0 <= z <= 1"),
    ("x > 1", "y > 1", "z > 1")
]

for case in cases:
    x_case, y_case, z_case = case
    expression = F_xyz_expression(x_case, y_case, z_case)
    print(f"F({x_case}, {y_case}, {z_case}) = {expression}")
