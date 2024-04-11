#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 1: Escribir un programa que valide la edad de una persona para que sea mayor de edad (mayor o igual a 18 años). En el caso que sea menor de edad o la edad sea incorrecta informar tal situación.

edad=int(input("ingrese su edad: "))
if edad>=18:
    print("la persona es mayor de edad")
else:
    print("la persona es menor de edad")