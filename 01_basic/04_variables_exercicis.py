###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

datos = {
    "nombre": "Movistar",
    "ubicacion": "Q1/1003",
    "puertos": 4,
    "encendido": True
}
print(f"""  
      encaminador: {datos['nombre']};
      ubicación: {datos['ubicacion']};
      puertos: {datos['puertos']};
      encendido: {datos['encendido']}""")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
GB_inc=20
GB_con=10.74
GB_restant = GB_inc - GB_con
print(f"GB restants: {GB_restant:.2f}")
GB_con = 15.25
GB_restant = GB_inc - GB_con
print(f"GB restants: {GB_restant:.2f}")