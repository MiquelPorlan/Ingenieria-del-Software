numSecreto = 7
num = 0
while num != numSecreto:
    num = int(input("intenta adivinar el numero secreto:"))
    if num < numSecreto:
        print("el numero secreto es mayor")
    elif num > numSecreto:
        print("el numero secreto es menor")