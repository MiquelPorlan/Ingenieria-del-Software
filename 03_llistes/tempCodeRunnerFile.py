llista_a = [1, 2, 3]
llista_b = [4, 5, 6, 1, 2]
llista_a.extend(llista_b)
llista_a.remove(1)
a = llista_a.pop(3)
llista_b.clear()
print(llista_a,llista_b,a,sep="\n")