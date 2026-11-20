###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.

def saludar_a(nom, salutacio="Hola"):
    print(f'{salutacio}, me llamo {nom}')
    
saludar_a('juan')
saludar_a('pepe','bonas')
saludar_a('peter',salutacio='yepa')

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
n = int(input())
def es_parell(numero):
    if numero%2==0:
        return True
    else:
        return False
if es_parell(n):
    print('si')
else:
    print('no')
    

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.

def mitjana(lista):
    suma = 0
    for n in lista:
        suma+=n
    return suma/len(lista)

print(mitjana([1,2,3]))

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.

def sumar_tot(*args):
    suma = 0
    for i in args:
        suma +=i
    return suma

print(sumar_tot(1,2))
print(sumar_tot(1,2,3,4,5))
print(sumar_tot(1,2,3,4,5,6,7,8,9,10))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().

def taula_multiplicar(numero, limit=10):
    for i in range(1,limit+1):
        t=numero*i
        print(f'{numero}*{i}={t}')

taula_multiplicar(2)
taula_multiplicar(2,3)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).

def mostrar_perfil(**kwargs):
  for clau, valor in kwargs.items():
    print(f"{clau}: {valor}")

mostrar_perfil(nom='Miquel', edat=21, grau='telecos')

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.

def factorial(f):
    f = 1
    while i>1:
        f *= i
        i -= 1
    return f
    
def maxim(lista):
    max=0
    for n in lista:
        if max<n:
            max=n
    return max
    