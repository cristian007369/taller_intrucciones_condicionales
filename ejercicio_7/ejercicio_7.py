# Programa para determinar si a+b=c

print("---------------------------------------------")
print("-------------------¿a+b=c?-------------------")
print("---------------------------------------------")

#Input

a=int(input("Dígite un número entero: "))
b=int(input("Ehhh dígite un número entero: "))
c=int(input("Otra vez lo mismo xD: "))
x=a+b

#Processing y output

if x==c:
    print("---------------------------------------------")
    print("La suma de a+b="+str(x)+"=c")
    print("---------------------------------------------")
else:
    print("---------------------------------------------")
    print("La suma de a+b="+str(x)+"≠c="+str(c))
    print("---------------------------------------------")