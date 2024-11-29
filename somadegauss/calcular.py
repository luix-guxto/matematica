import sys

args = sys.argv[1:]

def calcularSomaLista(primeiroValor,UltimoValor):
    t = (UltimoValor-primeiroValor)+1
    n1 = primeiroValor
    nt = UltimoValor
    return (t*(n1+nt)/2)

try: 
    print(calcularSomaLista(int(args[0]), int(args[1])))
except:
    print("Comando precisa de dois argumentos para funcionar ex:\npy calcular.py [primeiroValor] [ultimoValor]")