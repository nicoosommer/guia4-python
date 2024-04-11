#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 9:Codificar un programa que permita ingresar una frase por teclado e indique qué cantidad de palabras incluye.
frase=input("Ingrese una frase: ")
palabras=0
for i in frase:
    if i==" ":
        palabras+=1
print(f"La frase tiene {palabras+1} palabras")