import sys
import math

args = sys.argv[1:]

def calcularHipotenusa(catetoA, catetoO):
    cA = float(catetoA)
    cO = float(catetoO)
    return math.sqrt((cA*cA) + (cO*cO))

try:
    print(f'Valor da hipotenusa é: {calcularHipotenusa(args[0], args[1])}')
except:
    print(f'Favor inserir o valor do cateto Oposto e do Cateto Adjacente\nEX: py calcular.py 5 5')