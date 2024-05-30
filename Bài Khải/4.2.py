# Bài 4.2. Một lô hàng có 16 sản phẩm trong đó có 8 sản phẩm loại A, 5 sản phẩm loại B và 3 sản phẩm loại C. 
# Lấy ngẫu nhiên 3 sản phẩm từ lô hàng. 
# Gọi X là số sản phẩm loại A được lấy ra trong 3 sản phẩm; Y là số sản phẩm loại B được lấy từ ra trong 3 sản phẩm.  
# Lập bảng phân phối xác suất đồng thời (X, Y).

from math import comb as c
a=list()
for y in range (0,4):
    b=list()
    b.append(y)
    for x in range(0,4):
        z=3-x-y
        if z<0:
            d=0
        else:
            d=(c(8,x)*c(5,y)*c(3,z)/c(12,3))
        b.append(round(d,3))
    a.append(b)
print('bảng phân phối xác suất đồng thời (X, Y)')
format_table='| {:^5} | {:^5} | {:^5} | {:^5} | {:^5} |'
head=['y\\x',0,1,2,3]
print(format_table.format(*head))
for i in a:
    print(format_table.format(*i))