# Programa para determinar un prestamo bancario

print("--------------------------------------------------")
print("---------------------Banco------------------------")
print("--------------------------------------------------")

#Input

i=int(input("Por favor, indique cuanto gana mensualmente: "))
x=int(input("Dígite 1 si tiene deudas o 2 en caso de que no las tenga: "))

#Processing y output

if i>945200:
    if x==1:
        print("--------------------------------------------------")
        print("Lametamos informarle que no se te podrá otorgar el prestamo")
        print("--------------------------------------------------")
    else:
        print("--------------------------------------------------")
        print("Felicidades, cumples con los requisitos para el prestamo ")
        print("--------------------------------------------------")
else:
    print("--------------------------------------------------")
    print("Lametamos informarle que no se te podrá otorgar el prestamo")
    print("--------------------------------------------------")