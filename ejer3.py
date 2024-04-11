#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 3:Escribir un programa que solicite el nombre y el apellido de una persona e informe si los datos ingresados son incorrectos, mediante un mensaje de alerta y vuelva a solicitarlos (verificar que son caracteres y no son números).

nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
na=nombre+apellido
nums=["1","2","3","4","5","6","7","8","9","0"]
j=0
for i in na:
    if i in nums:
        print("EL nombre/apellido contiene numeros")
        j=1
        break
if j==0:
    print("EL nombre y apellido son correctos")