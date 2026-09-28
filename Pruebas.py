a = 10
b = 25
c = 40

def rango(Valor1):
    res = {
        (Valor1 < 20): -1,
        (Valor1 >= 20 and Valor1 <= 30): 0,
        (Valor1 > 30): 1,
    } [True]
    return res


print(rango(a))
print(rango(b))
print(rango(c))
