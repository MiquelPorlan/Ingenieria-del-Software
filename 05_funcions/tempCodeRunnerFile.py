print("\nExercici 6:")
def mostrar_perfil(**kwargs):
  for clau, valor in kwargs.items():
    print(f"{clau}: {valor}")

mostrar_perfil(nom='Miquel', edat=21, grau='telecos')