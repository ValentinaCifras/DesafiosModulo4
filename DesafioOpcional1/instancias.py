from te import Te
#REquerimiento 4
te_1 = Te()
te_2 = Te()

tipo_1 = type(te_1)
tipo_2 = type(te_2)

print(tipo_1)
print(tipo_2)

if tipo_1 == tipo_2:
    print("Los objetos son del mismo tipo")
else:
    print("Los objetos son de distinto tipo")