import math

# 1) Tìm hệ số A
def tim_he_so_A():
    # Tích phân kép để xác định A
    # Tích phân theo y từ 0 đến 1 và tích phân theo x từ 0 đến y
    def tich_phan(x, y):
        return 1 / math.sqrt(x * y)

    y_min, y_max = 0, 1

    # Tính tích phân theo phương pháp hình học
    tich_phan_ngoai = 0
    n = 1000  # Số lượng phần tử chia nhỏ
    delta_y = (y_max - y_min) / n

    for i in range(n):
        y = y_min + (i + 0.5) * delta_y
        x_min, x_max = 0, y
        delta_x = (x_max - x_min) / n
        
        tich_phan_trong = 0
        for j in range(n):
            x = x_min + (j + 0.5) * delta_x
            tich_phan_trong += tich_phan(x, y) * delta_x
        
        tich_phan_ngoai += tich_phan_trong * delta_y

    A = 1 / tich_phan_ngoai
    return A

A = tim_he_so_A()
print(f"Hệ số A: {round(A,2)}")

# 2) Tìm f_X(x) và f_Y(y)
def f_X():
    print("f_X(x) = (",round(A,2) * 2 ,"/ sqrt(x)) - 1   : nếu 0 < x <= 1")

def f_Y():
    print(f"f_y=",round(A*2),"nếu 0 <y<=1 ")

# In ra các hàm mật độ biên
f_X()
f_Y()

# 3) Xét tính độc lập của X và Y
def kiem_tra_doc_lap(A):
    # Xét f_X(x) * f_Y(y) và so sánh với f_{X,Y}(x,y)
    for y in [0.25, 0.5, 0.75]:  # Các giá trị y để kiểm tra
        for x in [0.25, 0.5, 0.75]:  # Các giá trị x để kiểm tra
            f_XY = (A / math.sqrt(x * y)) if (0 < x <= y <= 1) else 0
            if abs((A * 2 * math.sqrt(x)) * (A * 2 * y) - f_XY) > 1e-6:  
                return False
    return True

doc_lap = kiem_tra_doc_lap(A)
print(f"X và Y {'độc lập' if doc_lap else 'không độc lập'}")