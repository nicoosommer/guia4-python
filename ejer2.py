#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 2: Escribir un programa que valide si la edad de una persona es apta para solicitar la jubilación. Para nuestro ejemplo tomaremos como edad válida los 65 años. En el caso que le falten años para tal motivo, informar cuántos años le faltan.

edad=int(input("ingrese su edad: "))
if edad>=65:
    print("la persona es apta para la jubilacion")
else:
    print(f"la persona no es apta para la jubilacion, le faltan {65-edad} años para la jubilacion")