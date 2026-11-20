###
# EXERCICIS (diccionaris)
###

# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.

estudiante = {
    'nom': 'miquel',
    'edat': 21,
    'assignatures': ['calculo','señales discretas','circuitos']
}
print(estudiante)

# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.

print(estudiante['assignatures'][2])
estudiante['edat'] = 22

# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.

estudiante = {**estudiante,'grau': 'telecos'}
del estudiante['edat']

# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.

print('nom' in estudiante)
print('email' in estudiante)

# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".


for clau, valor in estudiante.items():
  print(f"{clau}: {valor}")

# Exercici 6: Comptar paraules
# Donada la llista de paraules:
# paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.

paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
dict1 = {}
for palabra in set(paraules):
    dict1 = {**dict1, palabra: paraules.count(palabra)}
print(dict1)