###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

Nom = input("Nom:")
Xarxa = input("Nom xarxa:")

print(f"Tecnic:{Nom}\nXarxa:{Xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

d = float(input("longitud de l'enllaç(km):"))
v = float(input("velocitat de transmisio(Gbps):"))

GBs = 8/v

print(f"enllaç de {d}, temps de transmisio {GBs}")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

h = float(input("temps de instalacion(h):"))
ph = float(input("precio por hora(€):"))
mat = float(input("precio materiales(€)"))

print(f"precio final: {h*ph+mat}")
