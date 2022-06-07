

from posixpath import split
from re import X
from tkinter import N

##############################################################
# functions

def movimentos (pos_ini_x1, pos_ini_y1, nswe1, n_commands1):

    nm = 0
    
    
    while nm < n_commands1:

        if nswe1 in ['n', 'N']:

            if movimentos1[nm] in ['l', 'L']:
                nm + 1
                nswe1 = 'W'
            elif movimentos1[nm] in ['r', 'R']:
                nm + 1
                nswe1 = 'E'
            elif movimentos1[nm] in ['m', 'M']:
                nm + 1
                pos_ini_y1 + 1

        elif nswe1 in ['s', 'S']:
            if movimentos1[nm] in ['l', 'L']:
                nm + 1
                nswe1 = 'E'
            elif movimentos1[nm] in ['r', 'R']:
                nm + 1
                nswe1 = 'W'
            elif movimentos1[nm] in ['m', 'M']:
                nm + 1
                pos_ini_y1 - 1


        elif nswe1 in ['w', 'W']:
            if movimentos1[nm] in ['l', 'L']:
                nm + 1
                nswe1 = 'S'
            elif movimentos1[nm] in ['r', 'R']:
                nm + 1
                nswe1 = 'N'
            elif movimentos1[nm] in ['m', 'M']:
                nm + 1
                pos_ini_x1 - 1

        elif nswe1 in ['e', 'E']:
            if movimentos1[nm] in ['l', 'L']:
                nm + 1
                nswe1 = 'N'
            elif movimentos1[nm] in ['r', 'R']:
                nm + 1
                nswe1 = 'S'
            elif movimentos1[nm] in ['m', 'M']:
                nm + 1
                pos_ini_x1 + 1

    return(pos_ini_x1, pos_ini_y1, nswe1)

##############################################################
# coordenadas

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


##############################################################
# posição inicial sonda 1

pos_ini_x1s,pos_ini_y1s, nswe1 = input("insira a coordenada inicial da sonda 1: ").split()

pos_ini_x1 = int(pos_ini_x1s)
pos_ini_y1 = int(pos_ini_y1s)


##############################################################
# comandos de movimentações sonda 1

movimentos1 = input("insira as instruções de movimentações da sonda 1: ")
movimentos1 = list(movimentos1)
n_commands1 = len(movimentos1)

movimentos(pos_ini_x1, pos_ini_y1, nswe1, n_commands1)


##############################################################
# posição inicial sonda 2

#pos_ini_x2s,pos_ini_y2s, nswe2 = input("insira a coordenada inicial da sonda 2: ").split()

#pos_ini_x2 = int(pos_ini_x2s)
#pos_ini_y2 = int(pos_ini_y2s)

#print(pos_ini_x2, pos_ini_y2, nswe2)

##############################################################
# comandos de movimentações sonda 2


##############################################################
# Output

print(pos_ini_x1, pos_ini_y1, nswe1)