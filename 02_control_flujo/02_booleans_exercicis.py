###
# EXERCICIS
###

# Exercici 1: Comparar nombres
# Donats els nombres:
# nombre_a = 8
# nombre_b = 5
# Mostra el resultat de comparar si nombre_a és més gran, més petit o igual
# que nombre_b.

a = 8
b = 5
print(f"{a} > {b} => {a > b}")
print(f"{a} < {b} => {a < b}")
print(f"{a} == {b} => {a == b}")

# Exercici 2: Comparar cadenes de text
# Donades les cadenes:
# paraula_a = "Hola"
# paraula_b = "hola"
# Mostra si són iguals i si paraula_a és igual a "Hola".
# Observa si Python distingeix entre majúscules i minúscules.

a = "hola"
b = "Hola"
print(f"{a} == {b} => {a == b}")

# Exercici 3: Connexió de xarxa
# Donats els valors booleans:
# router_encès = True
# connexio_activa = False
# Crea una variable anomenada xarxa_disponible que sigui True només si el
# router està encès i la connexió està activa. Mostra'n el resultat.

router = True
connexio = False
xarxa = router & connexio
print(f"xarxa activa => {xarxa}")

# Exercici 4: Avisos pendents
# Donats els valors booleans:
# actualitzacio_disponible = False
# alerta_critica = True
# Crea una variable anomenada cal_avisar que sigui True si hi ha una
# actualització disponible o una alerta crítica. Mostra'n el resultat.

actualitzacio_disponible = False
alerta_critica = True
cal_avisar = alerta_critica | actualitzacio_disponible
print(f"cal avisar => {cal_avisar}")

# Exercici 5: Accés a un compte
# Donats els valors booleans:
# compte_actiu = True
# contrasenya_correcta = True
# codi_correcte = False
# dispositiu_de_confiança = True
# compte_bloquejat = False
# Crea una variable anomenada accés_permes que sigui True si el compte està
# actiu, la contrasenya és correcta, el compte no està bloquejat i, a més,
# el codi és correcte o el dispositiu és de confiança. Fes servir and, or i not.
# Mostra'n el resultat.

compte_actiu = True
contrasenya_correcta = True
codi_correcte = False
dispositiu_de_confiança = True
compte_bloquejat = False
acces_permes = compte_actiu & contrasenya_correcta & (not compte_bloquejat) & (codi_correcte | dispositiu_de_confiança)