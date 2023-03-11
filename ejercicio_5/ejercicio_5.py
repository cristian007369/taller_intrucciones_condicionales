#Programa que permite determinar el gasto de agua 

print("---------------------------------------------")
print("--------------Gasto de agua------------------")
print("---------------------------------------------")

#input

x=int(input("Ingrese el valor de agua consumida en m^3: "))

#Processing y output

if x<=50:
    print("---------------------------------------------")
    print("El gato es de 10000 ")
    print("---------------------------------------------")
else:
    if x<=200:
        y=10000+x*2000
        print("---------------------------------------------")
        print("El gato es de " +str(y))
        print("---------------------------------------------")
    else:
        y=10000+x*3000
        print("---------------------------------------------")
        print("El gato es de " +str(y))
        print("---------------------------------------------")