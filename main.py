print("Solución de una ecuación cuadrática")
a=int(input("Ingrese el primer valor:"))
b=int(input("Ingrese el segundo valor:"))
c=int(input("Ingrese el tercer valor:"))
d=(((b*b)-(4*a*c))**1/2)
x1=(((-1*b)+(d**1/2))/2*a)
x2=(((-1*b)-(d**1/2))/2*a)
if d>0:
	print("La solución positiva es:",x1,"y la solución negativa es:",x2)
else:
	if d==0:
		(-1*b)/2*a
	else:
		if d<0:
			print("No existe solución en los números reales")

