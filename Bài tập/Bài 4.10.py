import numpy as np
import pandas as pd

# Tạo DataFrame từ bảng đã cho
du_lieu = {
    90: [0.04, 0.02, 0.17, 0.09],
    110: [0.07, 0.14, 0.17, 0.0],
    130: [0.02, 0.06, 0.12, 0.09],
    150: [0.0, 0.07, 0.08, 0.04],
    180: [0.0, 0.0, 0.06, 0.02]
}
chi_so_X = [4, 7, 12, 17]
df = pd.DataFrame(du_lieu, index=chi_so_X)
df.index.name = 'X'
df.columns.name = 'Y'
print("Bảng dữ liệu:")
print(df)

# Tổng xác suất để kiểm tra dữ liệu
tong_xac_suat = df.values.sum()
print("Tổng xác suất:", tong_xac_suat)

# Phân phối xác suất của X
phan_phoi_X = df.sum(axis=1)
print("Phân phối xác suất của X:")
print(phan_phoi_X)

# Phân phối xác suất của Y
phan_phoi_Y = df.sum(axis=0)
print("Phân phối xác suất của Y:")
print(phan_phoi_Y)

# Phân phối xác suất của X khi Y = 130
phan_phoi_X_khi_Y_130 = df[130] / phan_phoi_Y[130]
print("Phân phối xác suất của X khi Y = 130:")
print(phan_phoi_X_khi_Y_130)

# Phân phối xác suất của Y khi X = 12
phan_phoi_Y_khi_X_12 = df.loc[12] / phan_phoi_X[12]
print("Phân phối xác suất của Y khi X = 12:")
print(phan_phoi_Y_khi_X_12)

# Kiểm tra tính độc lập của X và Y
doc_lap = True
for x in df.index:
    for y in df.columns:
        if not np.isclose(df.loc[x, y], phan_phoi_X[x] * phan_phoi_Y[y]):
            doc_lap = False
            break
    if not doc_lap:
        break

print("X và Y có độc lập không?", doc_lap)