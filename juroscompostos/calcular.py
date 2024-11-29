import sys
import math

args = sys.argv[1:]

# M: Montante total (valor final acumulado).
# P: Capital inicial (valor investido inicialmente).
# A: Valor do aporte mensal (valor adicionado regularmente).
# i: Taxa de juros (por período, geralmente mensal, em decimal: taxa/100).
# n: Número total de períodos (geralmente em meses).

def calcularJuros(P, A, i, n):
    P = float(P)
    A = float(A)
    i = (float(i))/100
    n = float(n)

    cresCapInic = P * ((1 + i)**n)
    cresAport = (A*(((1+i)**n)-1))/i

    M = cresAport + cresCapInic
    return M

def calcularAporte(P, A, n):
    P = float(P)
    A = float(A)
    n = float(n)

    return P+(A*n)

try: 
    g_P = args[0]
    g_A = args[1]
    g_i = args[2]
    g_n = args[3]

    totalAporte = calcularAporte(g_P, g_A, g_n)
    totalFinal = calcularJuros(g_P, g_A, g_i, g_n)
    totalJuros = totalFinal - totalAporte
    print(f'Capital Inicial: {g_P}\nValor Aporte mensal: {g_A}\ntaxa de juros mensal: {g_i}\nNumero de meses: {g_n}\ntotal aportado: {totalAporte}\ntotal final: {totalFinal}\ntotal de juros: {totalJuros}')
except:
    print(f'Favor inserir o valor do P: Capital inicial (valor investido inicialmente). A: Valor do aporte mensal (valor adicionado regularmente). i: Taxa de juros (por período, geralmente mensal, em decimal: taxa/100). n: Número total de períodos (geralmente em meses).\nEX: py calcular.py P A i n')