# Programa sobre el plano cartesiano

print("----------------------------------------")
print("----------Plano Cartesiano--------------")
print("----------------------------------------")

#Input

x=int(input("Dígite el valor de X: "))
y=int(input("Dígite el valor de y: "))

#Processing y output

if x==0 and y==0:
    print("----------------------------------------")
    print("El Punto está en el origen (0,0)")
    print("----------------------------------------")
else:
    if x==0:
        print("----------------------------------------")
        print("El punto está sobre el eje Y en la coordenada (0,"+ str(x) + ")")
        print("----------------------------------------")
    else:
        if y==0:
           print("----------------------------------------")
           print("El punto está sobre el eje X en la coordenada ("+ str(x) + ",0)")
           print("----------------------------------------") 
        else:
            if x>0:
                if y>0:
                    print("----------------------------------------")
                    print("El punto está en el cuadrante I en la coordenada ("+str(x)+","+str(y)+")")
                    print("----------------------------------------")
                else:
                    print("----------------------------------------")
                    print("El punto está en el cuadrante IV en la coordenada ("+str(x)+","+str(y)+")")
                    print("----------------------------------------")
            else:
                if y>0:
                    print("----------------------------------------")
                    print("El punto está en el cuadrante II en la coordenada ("+str(x)+","+str(y)+")")
                    print("----------------------------------------")
                else:
                    print("----------------------------------------")
                    print("El punto está en el cuadrante III en la coordenada ("+str(x)+","+str(y)+")")
                    print("----------------------------------------")