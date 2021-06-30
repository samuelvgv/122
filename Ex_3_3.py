def diferencia_edad_perro_humano(edad_persona):
    if edad_persona<= 2:
        return edad_persona*10.5
    else:
        return 21+(edad_persona - 2)*4
    
edad_persona = int (input('inserte edad de la persona'))
if edad_persona>0:
    total = diferencia_edad_perro_humano(edad_persona)
    print(f'la edad del perro en los años humanos es:',total)
    