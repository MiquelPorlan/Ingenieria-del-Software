paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
dict1 = {}
for palabra in set(paraules):
    dict1 = {**dict1, palabra: paraules.count(palabra)}
print(dict1)