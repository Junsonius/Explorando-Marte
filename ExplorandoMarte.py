

from posixpath import split
from re import X
from tkinter import N

##############################################################
# functions

def movimentos (pos_ini_x, pos_ini_y, nswe, n_commands, movimentos, x, y):

    nm = 0
    
    
    while nm < n_commands:
    
        if nswe in ['n', 'N']:
        
            if movimentos[nm] in ['l', 'L']:
                nm+= 1
                nswe = 'W'
            elif movimentos[nm] in ['r', 'R']:
                nm+= 1
                nswe = 'E'
            elif movimentos[nm] in ['m', 'M']:
                nm+= 1
                pos_ini_y+= 1
                if pos_ini_y > y:
                    pos_ini_y-= 1
                    print("não é possível realizar movimento \npois está fora da malha do planalto")

        elif nswe in ['s', 'S']:
            if movimentos[nm] in ['l', 'L']:
                nm+= 1
                nswe = 'E'
            elif movimentos[nm] in ['r', 'R']:
                nm+= 1
                nswe = 'W'
            elif movimentos[nm] in ['m', 'M']:
                nm+= 1
                pos_ini_y-= 1
                if pos_ini_y < 0:
                    pos_ini_y+= 1
                    print("não é possível realizar movimento \npois está fora da malha do planalto")


        elif nswe in ['w', 'W']:
            if movimentos[nm] in ['l', 'L']:
                nm+= 1
                nswe = 'S'
            elif movimentos[nm] in ['r', 'R']:
                nm+= 1
                nswe = 'N'
            elif movimentos[nm] in ['m', 'M']:
                nm+= 1
                pos_ini_x-= 1
                if pos_ini_x > x:
                    pos_ini_x-= 1
                    print("não é possível realizar movimento \npois está fora da malha do planalto")

        elif nswe in ['e', 'E']:
            if movimentos[nm] in ['l', 'L']:
                nm+= 1
                nswe = 'N'
            elif movimentos[nm] in ['r', 'R']:
                nm+= 1
                nswe = 'S'
            elif movimentos[nm] in ['m' , 'M']:
                nm+= 1
                pos_ini_x+= 1
                if pos_ini_x < 0:
                    pos_ini_y+= 1
                    print("não é possível realizar movimento \npois está fora da malha do planalto")

    return(pos_ini_x, pos_ini_y, nswe)

##############################################################
# coordenadas

terreno_x = []
terreno_y = []

xs,ys = input("insira o tamanho do terreno: ").split()

x = int(xs)
y= int(ys)

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

result = movimentos(pos_ini_x1, pos_ini_y1, nswe1, n_commands1, movimentos1, x, y)
result = list(result)

pos_res_x1 = result[0]
pos_res_y1 = result [1]
nswe1res = result[2]


##############################################################
# posição inicial sonda 2

pos_ini_x2s,pos_ini_y2s, nswe2 = input("insira a coordenada inicial da sonda 2: ").split()

pos_ini_x2 = int(pos_ini_x2s)
pos_ini_y2 = int(pos_ini_y2s)


##############################################################
# comandos de movimentações sonda 2

movimentos2 = input("insira as instruções de movimentações da sonda 2: ")
movimentos2 = list(movimentos2)
n_commands2 = len(movimentos2)

result = movimentos(pos_ini_x2, pos_ini_y2, nswe2, n_commands2, movimentos2, x, y)
result = list(result)

pos_res_x2 = result[0]
pos_res_y2 = result [1]
nswe2res = result[2]


##############################################################
# Output

print(pos_res_x1, pos_res_y1, nswe1res)
print(pos_res_x2, pos_res_y2, nswe2res)