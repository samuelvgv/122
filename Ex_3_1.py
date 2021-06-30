print("Ventas de 3 productos")
A=int(input("coloque la primera venta"))
B=int(input("coloque la segunda venta"))
C=int(input("coloque la tercera venta"))
if (A>=B) or (A>=C):
     print("La primera venta fue la mas alta de todas")
else:
    print("La primera venta no fue la mas alta")

if (A<200) or (B<200) or (C<200):
    print("existen venta menores a 200")
else:
    print("Ningun venta es menor de 200")
if (A>400) or (B>400) or (C>400):
    print("Existen venta mayores de 400")
else:
   print("Ninguna venta es mayor a 400")
M=((A+B+C)/2)
if (M>500):
    print("La media es superior")
else:
    print("La media no es superior")
if (A>B) or (C>B):
    print("El producto B fue el menos vendido")
else:
    print("El producto B fue uno de los mas vendidos")
    
T=(A+B+C) 
if (T>500) or (T<1000):
    print("total de venta esta entre 500 y 1000")
else:
    print("Total de la venta fue mayor o menor a 500 o 1000")  