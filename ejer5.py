#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 5: Escribir un programa en Python que capture por teclado una lista de 7 nombres de persona, verifique que no son números y que estén ordenados alfabéticamente. 
nombre1=input("ingrese un nombre: ")
nombre2=input("ingrese otro nombre: ")
nombre3=input("ingrese otro nombre: ")
nombre4=input("ingrese otro nombre: ")
nombre5=input("ingrese otro nombre: ")
nombre6=input("ingrese otro nombre: ")
nombre7=input("ingrese otro nombre: ")
nums=["1","2","3","4","5","6","7","8","9","0"]
nombres=[nombre1,nombre2,nombre3,nombre4,nombre5,nombre6,nombre7]
j=0
for i in nombres:
    for f in i:
        if f in nums:
            j=1
            break
    if j==1:
        print("Un nombre contiene numeros")
        break
names=sorted(nombres)
if names!=nombres:
    j=1
    print("La lista no estaba en orden alfabetica")
if j==0:
    print("Todo fue ingresado correctamente")



