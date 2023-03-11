#Programa que determina si a multp b o viceversa 

print("---------------------------------------------")
print("------------------Multp----------------------")
print("---------------------------------------------")

#input

a=int(input("Dígite un número entero: "))
b=int(input("Dígite un número entero: "))

#Processing y output

x=a%b
y=b%a
if x==0 or y==0:
    if x==0:
        print("---------------------------------------------")
        print(str(a)+" es multiplo de "+str(b))
        print("---------------------------------------------")
    else:
        print("---------------------------------------------")
        print(str(b)+" es multiplo de "+str(a))
        print("---------------------------------------------")
    
else:
    y=x+x*0.15
    print("---------------------------------------------")
    print("Ninguno de los dos números es multiplo del otro")
    print("---------------------------------------------")