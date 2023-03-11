#Programa que permite determinar el precio de un producto

print("---------------------------------------------")
print("------------------Precio---------------------")
print("---------------------------------------------")

#input

x=int(input("Ingrese el costo del producto: "))

#Processing y output

if x<3000:
    y=x+x*0.15
    print("---------------------------------------------")
    print("El precio del del producto debe ser de: " +str(y))
    print("---------------------------------------------")
else:
    if x<=6000:
        y=x+500
        print("---------------------------------------------")
        print("El precio del del producto debe ser de: " +str(y))
        print("---------------------------------------------")
    else:
        y=x+x*0.25
        print("---------------------------------------------")
        print("El precio del del producto debe ser de: " +str(y))
        print("---------------------------------------------")
