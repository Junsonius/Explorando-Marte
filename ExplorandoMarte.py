# coordenadas

from posixpath import split
from re import X

terreno_x = []
terreno_y = []

xs,ys = input("insira o tamanho do terreno: ").split()

xi = int(xs)
yi= int(ys)

x = 0
y = 0

while x <= xi:
    terreno_x.append(x)
    x = x + 1
  

while y <= yi:
    terreno_y.append(y)
    y = y + 1

print(terreno_x)
print(terreno_y)

##############################################################
# posição inicial sonda 1

pos_ini_x1s,pos_ini_y1s, nswe1 = input("insira a coordenada inicial da sonda 1: ").split()

pos_ini_x1 = int(pos_ini_x1s)
pos_ini_y1 = int(pos_ini_y1s)

print(pos_ini_x1, pos_ini_y1, nswe1)

##############################################################
# comandos de movimentações sonda 1

movimentos1 = input("insira as instruções de movimentações da sonda 1: ")
movimentos1 = list(movimentos1)
print (movimentos1)

##############################################################
# comandos de movimentações sonda 2



##############################################################
# posição inicial sonda 2

pos_ini_x2s,pos_ini_y2s, nswe2 = input("insira a coordenada inicial da sonda 2: ").split()

pos_ini_x2 = int(pos_ini_x2s)
pos_ini_y2 = int(pos_ini_y2s)

print(pos_ini_x2, pos_ini_y2, nswe2)


##############################################################
# Output

