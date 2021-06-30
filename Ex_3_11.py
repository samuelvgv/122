print('coloca las coordenadas:')
ax=float(input("punto x en la primera coordenada:"))
ay=float(input('punto y en la primera coordenada:'))
bx=float(input("punto x en la segunda coordenada:"))
by=float(input("punto y en la segunda coordenada:"))
#operaciones
A=(ax+ay)/2
B=(bx+by)/2
M=A+B
print('la media en los dos puntos son=', M)
if (A>0 and B>0):
    print('pertenece al primer cuadrante')
else:
    if (A<0 and B>0):
        print('pertenece al segundo cuadrante')
    else:
        if A<0 and B<0:
            print('pertenece al tercer cuadrante')
        else:
            if A>0 and B<0:
                print('pertenece al cuarto cuadrante')
            else:
                if A!=0 and B==0:
                    print('se situa en el eje x')
                else:
                    if A==0 and B!=0:
                        print('se situa en el eje y')
                    else:
                        print('esta en el punto origen')