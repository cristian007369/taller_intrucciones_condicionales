#Programa que permite determinar si un triangulo es obtuso,recto o agudo

print("---------------------------------------------")
print("------------------Triangulo------------------")
print("---------------------------------------------")

#Input

import math
a=int(input("Ingrese el valor de un lado del triangulo: "))
b=int(input("Ingrese el valor de otro lado del triangulo: "))
c=int(input("Ingrese el valor del ultimo lado del triangulo: "))

#Processing
e=a**2
f=b**2
h=c**2
e1=f+h-e
f1=e+h-f
h1=f+e-h
e2=2*c*b
f2=2*a*c
h2=2*a*b
x=e1/e2
y=f1/f2
z=h1/h2
alfa=math.acos(x)
beta=math.acos(y)
cc=math.acos(z)
alfa=round(alfa*180/math.pi,2)
beta=round(beta*180/math.pi,2)
cc=round(cc*180/math.pi,2)

#Output

if alfa<=60 and beta<=60 and cc<=60:
    print("---------------------------------------------")
    print("Angulo alfa = "+str(alfa))
    print("Angulo beta = "+str(beta))
    print("Angulo gamma = "+str(cc))
    print("---------------------------------------------")
    print("El triangulo es agudo")
    print("---------------------------------------------")
else:
    if alfa>90 or beta>90 or cc>90:
        print("---------------------------------------------")
        print("Angulo alfa = "+str(alfa))
        print("Angulo beta = "+str(beta))
        print("Angulo gamma = "+str(cc))
        print("---------------------------------------------")
        print("El triangulo es obtuso")
        print("---------------------------------------------")
    else:
        print("---------------------------------------------")
        print("Angulo alfa = "+str(alfa))
        print("Angulo beta = "+str(beta))
        print("Angulo gamma = "+str(cc))
        print("---------------------------------------------")
        print("El triangulo es recto")
        print("---------------------------------------------")