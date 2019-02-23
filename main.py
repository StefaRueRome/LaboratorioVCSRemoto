num=int(input("Introduzca un número para calcular su cuadrado:"))
cuadrado=(num*num)
print("El cuadrado del número es:",cuadrado)

num2=int(input("Introduzca un número para calcular su raiz cuadrada:"))
raiz_cuadrada=(num2**(1/2))
if num2<0:
	print("El número no tiene raiz cuadrada definida")
else:
	print("La raiz cuadrada es:",raiz_cuadrada)