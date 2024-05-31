import numpy as np
import matplotlib.pyplot as plt

# Bảng phân phối xác suất của X
Gia_tri_X = [0, 1, 2, 3, 4]
Xac_suat_X = [0.05, 0.15, 0.4, 0.3]
p = 1 - sum(Xac_suat_X)
Xac_suat_X.append(p)

# 1) Tính giá trị của p và xác suất số hợp đồng là từ 2 trở lên
Xac_suat_2_tro_len = sum(Xac_suat_X[2:])
print(f"1) Giá trị của p: {p:.2f}")
print(f"   Xác suất số hợp đồng là từ 2 trở lên: {Xac_suat_2_tro_len:.2f}")

# 2) Tính hàm khối lượng xác suất (bảng phân phối xác suất của X)
print("2) Hàm khối lượng xác suất là:")
for x, px in zip(Gia_tri_X, Xac_suat_X):
    print(f"   P(X = {x}): {px:.2f}")

# Vẽ biểu đồ phân phối xác suất của số hợp đồng ký được
plt.bar(Gia_tri_X, Xac_suat_X, tick_label=Gia_tri_X)
plt.xlabel("Số hợp đồng ký được")
plt.ylabel("Xác suất")
plt.title("Biểu đồ phân phối xác suất của số hợp đồng ký được")
plt.grid()
plt.show()

# 3) Tính kỳ vọng và phương sai của số hợp đồng kí được
E_X = np.sum(np.array(Gia_tri_X) * np.array(Xac_suat_X))
Var_X = np.sum(((np.array(Gia_tri_X) - E_X) ** 2) * np.array(Xac_suat_X))
print(f"3) Kỳ vọng của số hợp đồng ký được: {E_X:.2f}")
print(f"   Phương sai của số hợp đồng ký được: {Var_X:.4f}")

# 4) Tính kỳ vọng và phương sai của lợi nhuận
Loi_nhuan_tren_hop_dong = 100  # triệu đồng
Gia_tri_Loi_nhuan = [x * Loi_nhuan_tren_hop_dong for x in Gia_tri_X]
Ky_vong_Loi_nhuan = Loi_nhuan_tren_hop_dong * E_X
Phuong_sai_Loi_nhuan = (Loi_nhuan_tren_hop_dong ** 2) * Var_X
print(f"4) Kỳ vọng của lợi nhuận: {Ky_vong_Loi_nhuan:.2f} triệu đồng")
print(f"   Phương sai của lợi nhuận: {Phuong_sai_Loi_nhuan:.2f} triệu đồng^2")

# Vẽ biểu đồ phân phối xác suất của lợi nhuận
plt.bar(Gia_tri_Loi_nhuan, Xac_suat_X, tick_label=Gia_tri_Loi_nhuan, width=80)
plt.xlabel("Lợi nhuận (triệu đồng)")
plt.ylabel("Xác suất")
plt.title("Biểu đồ phân phối xác suất của lợi nhuận")
plt.grid()
plt.show()
