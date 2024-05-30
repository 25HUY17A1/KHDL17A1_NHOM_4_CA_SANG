# Bài 4.4. Ta có hai hộp, mỗi hộp có 6 viên bi: 
#Hộp I có một bi mang số 1, hai bi số 2 và ba bi số 3. 
#Hộp II có hai bi mang số 1, ba bi số 2 và một bi số 3. 	 
#Gọi X và Y tương ứng là số hiệu của viên bi tương ứng chọn ngẫu nhiên từ hai hộp (mỗi hộp chọn một bi). 
#Xây dựng bảng phân phối của cặp biến (X,Y) và chứng tỏ rằng X và Y độc lập nhau. 

from math import comb as c
a=list()
h1=[1,2,3]
h2=[2,3,1]
i=1
for y in h2:
    b=list()
    b.append(i)
    i+=1
    for x in h1:
        d=(c(x,1)/c(6,1))*(c(y,1)/c(6,1))
        b.append(round(d,2))
    a.append(b)
print(a)
print('bảng phân phối của cặp biến (X,Y)')
format_table='| {:^5} | {:^5} | {:^5} | {:^5} |'
head=['y\\x',1,2,3]
print(format_table.format(*head))
for i in a:
    print(format_table.format(*i))

#chứng minh X và Y độc lập nhau
x=0
for i in a:
    x+=i[1]
c=round(x*sum(a[0][1:]),2)
if c==a[0][1]:
    print('\nX và Y độc lập')
else:
    print('\nX và Y không độc lập')