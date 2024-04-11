#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 6: Crear un programa que permita ingresar los lados válidos de un triángulo y calcule su perímetro y su área.
while True:
    lado1=int(input("Ingrese el lado 1: "))
    lado2=int(input("Ingrese el lado 2: "))
    lado3=int(input("Ingrese el lado 3: "))
    if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
        break
    else:
        print("Los lados no son validos para un triangulo. Ingreselo de nuevo.")
perimetro=lado1+lado2+lado3
s=(lado1+lado2+lado3)/2
area=(s*(s-lado1)*(s-lado2)*(s-lado3))**.5
print(f"EL perimetro es {perimetro} y el area es {area}")