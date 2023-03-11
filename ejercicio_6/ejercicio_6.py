#Programa de la ecuación cuadrática

print("---------------------------------------------")
print("----------------Ecuación ^2------------------")
print("---------------------------------------------")

#Input

import math
a=int(input("Dígite el valor del coeficiente a: "))
b=int(input("Dígite el valor del coeficiente b: "))
c=int(input("Dígite el valor del coeficiente c: "))
d=b*b-4*a*c

#Processing y output

if a==0:
    w=-b/c
    print("---------------------------------------------------")
    print("La solución de la ecuación es x= "+str(w))
    print("---------------------------------------------------")
else:
    if d>0:
        w1=(-b+math.sqrt(d))/2*a
        w2=(-b-math.sqrt(d))/2*a
        print("---------------------------------------------------")
        print("Las soluciones de la ecuación son: x1="+str(w1)+" y x2="+str(w2))
        print("---------------------------------------------------")
    else:
        if d==0:
            w=-b/2*a
            print("---------------------------------------------------")
            print("La solución de la ecuación es x= "+str(w))
            print("---------------------------------------------------")
        else:
            print("---------------------------------------------------")
            print("La ecuación no tiene solución entre los reales")
            print("---------------------------------------------------")