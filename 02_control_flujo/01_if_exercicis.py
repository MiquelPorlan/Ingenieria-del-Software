###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

nivel = float(input("Introduce el nivel de la senyal recibida en dBm"))
if (nivel > -50):
    print("excelente")
elif (nivel > -67):
    print("bona")
elif (nivel > -75):
    print("debil")
else:
    print("muy debil")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

pot = float(input("cual es la potencia optima recibida en dBm"))
if (nivel < -27 ):
    print("muy baja")
elif (nivel <= -8 ):
    print("aceptable")
else:
    print("demasiado alto")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
GBplan = 20
GBcons = float(input("cual es la potencia optima recibida en dBm"))
if (GBcons > GBplan):
    print(f"limite mensual superado por {GBcons - GBplan}")
else :
    print("limite mensual no superado")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

LOSTerminal = input("El indicador LOS de la terminal esta encendido (y/n)")
Internet = input("El indicador de Internet en el Router esta encendido (y/n)")
if ((LOSTerminal == y | LOSTerminal == Y) & (Internet == y | Internet == Y) ):
    print("servicio funcionando correctamente")
if ((LOSTerminal == y | LOSTerminal == Y) & (Internet == n | Internet == N) ):
    print("porfavor comprueba el servicio con el provedor")    
if ((LOSTerminal == n | LOSTerminal == N)):
    print("Porfavor revise la conexion de fibra optica")
    
# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bateria = float(input("inttroduce el nivel de bateria"))
if (bateria >= 0 & bateria <= 100):
    if (bateria < 20 ):
        print("nivel critico")
    elif (bateria < 49 ):
        print("nivel bajo")
    else:
        print("nivel suficiente")
else:
    print("valor fuera de rango")