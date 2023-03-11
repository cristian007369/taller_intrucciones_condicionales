#Programa para calcular el IMC y dar diagnósticos 

print("---------------------------------------------")
print("--------------------IMC----------------------")
print("---------------------------------------------")

#Input

p=float(input("Ingrese su peso actual en Kg: "))
h=float(input("Ingrese su altura en m: "))
i=round(p/h**2,2)

#Processing y output

if i<16:
    print("Criterio ingreso en hospital, IMC="+str(i))
else:
    if i<=17:
        print("---------------------------------------------")
        print("Infrapeso, IMC="+str(i))
        print("---------------------------------------------")
    else:
        if i<=18:
            print("---------------------------------------------")
            print("Bajo de peso, IMC="+str(i))
            print("---------------------------------------------")
        else:
            if i<=25:
                print("---------------------------------------------")
                print("Peso normal (Saludable), IMC="+str(i))
                print("---------------------------------------------")
            else:
                if i<=30:
                    print("---------------------------------------------")
                    print("Sobrepeso (Obesidad grado I), IMC="+str(i))
                    print("---------------------------------------------")
                else:
                    if i<=35:
                        print("---------------------------------------------")
                        print("Obesidad crónica (Obesidad grado II), IMC="+str(i))
                        print("---------------------------------------------")
                    else:
                        if i<=40:
                            print("---------------------------------------------")
                            print("Obesida premórbida (Obesidad grado III), IMC="+str(i))
                            print("---------------------------------------------")
                        else:
                            print("---------------------------------------------")
                            print("Obesida mórbida (Obesida grado IV), IMC="+str(i))
                            print("---------------------------------------------")