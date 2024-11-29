import sys
import math

args = sys.argv[1:]

# 1x2 -4x +3 = 0
# (1) is a (- 4) is b (+ 3) is c

def calcular(a, b, c):
    a = a.split("x")[0]
    doubleA = 0
    if '-' in a:
        doubleA = float(a.replace("-",''))*-1
    else:
        doubleA = float(a.replace("+",''))
    b = b.split("x")[0]
    doubleb = 0
    if '-' in a:
        doubleb = float(b.replace("-",''))*-1
    else:
        doubleb = float(b.replace("+",''))
    doublec = 0
    if '-' in c:
        doublec = float(c.replace("-",''))*-1
    else:
        doublec = float(c.replace("+",''))
    delta = (doubleb*doubleb)-(4*doubleA*doublec)
    x1 = ((-1*doubleb) - math.sqrt(delta))/(2*doubleA)
    x2 = ((-1*doubleb) + math.sqrt(delta))/(2*doubleA)

    print(f'Delta: {delta}\nx1: {x1}\nx2: {x2}')

try:
    calcular(args[0], args[1], args[2])
except:
    print(f'Favor inserir os valores de A, B e C no formato de equação. Ex:\npy calcular.py 1x2 -4x +3')