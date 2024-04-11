#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 7:Crear un programa que permita calcular las raíces de un “Polinomio de segundo grado” de la forma y = a x2 + b x + c e indique si sus raíces son complejas, en el caso que lo sean.
a=float(input("Ingrese el valor del coeficiente A: "))
b=float(input("Ingrese el valor del coeficiente B: "))
c=float(input("Ingrese el valor del coeficiente C: "))

discriminante=(b**2)-4*a*c
if discriminante<0:
    print("Las raices son complejas")
elif discriminante>0:
    x1=(-b+discriminante**.5)/(2*a)
    x2=(-b-discriminante**.5)/(2*a)
    print(f"El polinomio tiene 2 raices: {x1} y {x2}")
else:
    x=-b/(2*a)
    print(f"La raiz del polinomio es {x}")