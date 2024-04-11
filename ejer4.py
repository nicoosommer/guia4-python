#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 4: Escribir un programa que solicite 5 números enteros no repetidos por teclado y valide que son correctos: son enteros, y no son caracteres (letras o símbolos)
numeros=[]
for j in range(5):
    while True:
        num=input("Ingrese un numero: ")
        if num in numeros:
            print("El numero que ingreso ya se habia ingresado antes.")
        else:
            numeros.append(num)
            break
bandera=0
for i in numeros:
    if i.isnumeric()!=True:
        print("Hay uno o mas numeros no enteros o uno o mas numeros que contienen letras")
        bandera=1
        break
if bandera==0:
    print("Todos los numeros son correctos")

    

  