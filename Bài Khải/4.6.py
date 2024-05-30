# Cho phân phối xác suất đồng thời của biến ngẫu nhiên (X, Y) cho bởi bảng:
""" 
| x\y   | 1     | 2     | 3     |
| 6     | 0.1   | 0.05  | 0.15  |
| 7     | 0.05  | 0.15  | 0.1   |
| 8     | 0.1   | 0.2   | 0.1   |
"""
#1)	Lập bảng phân phối xác suất biên của X, Y; 
#2)	Tính E(X), E(Y), V(X), V(Y); 
#3)	Lập bảng phân phổi xác suất của Y với điều kiện X = 7; 
#4)	Tính P(X = 6) và P(X ≥ 7, Y ≥ 2). 

table=[[0.1,0.05,0.15],[0.05,0.15,0.1],[0.1,0.2,0.1]]

#lập bảng phân phối xác xuất biên của X và Y
#X
format_table='| {:^10} | {:^5} | {:^5} | {:^5} |'

print('bảng phân phối xác suất biên của X')
X=[6,7,8]
print(format_table.format(*(['X'] + X)))
Px=[]
for x in range(3):
    Px.append(round(sum(table[x]),2))    
print(format_table.format(*(['P(X)'] + Px)))

#Y
print('\nbảng phân phối xác suất biên của Y')
Y=[1,2,3]
print(format_table.format(*(['Y'] + Y)))    
Py=[]
for y in range(3):
    Py.append(round(table[0][y] + table[1][y] + table[2][y],2))
print(format_table.format(* (['P(Y)'] + Py)))


#Tính E(X), E(Y), V(X), V(Y)
print('\n')
#E(X)
Ex=0
for i in range(3):
    Ex+=X[i]*Px[i]
print(f'E(X) = {Ex:.2}')
#E(Y)
Ey=0
for i in range(3):
    Ey+=Y[i]*Py[i]
print(f'E(Y) = {Ey:.2}')
#V(X)
Vx = sum([(X[i]**2)*Px[i] for i in range(3)]) - Ex**2
print(f'V(X) = {Vx:.2}')
#V(Y)
Vy = sum([(Y[i]**2)*Py[i] for i in range(3)]) - Ey**2
print(f'V(Y) = {Vy:.2}\n')


#Lập bảng phân phổi xác suất của Y với điều kiện X = 7

PY7=[round(table[1][y]/Px[1],2) for y in range(3)]
print(format_table.format(*(['Y'] + Y)))
print(format_table.format(*(['P(Y|X=7)'] + PY7)))

#Tính P(X = 6) và P(X ≥ 7, Y ≥ 2)

#P(X = 6)
print(f'\nP(X=6) = {Px[0]} ')

#P(X ≥ 7, Y ≥ 2)
P72=0
for p in range(1,3):
    P72+= table[1][p] + table[2][p]
print(f'P(X ≥ 7, Y ≥ 2) = {P72}')