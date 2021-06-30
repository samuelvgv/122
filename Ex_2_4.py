print('Calculacion de segundos a dias, horas y minutos')
s=int(input('segundos a transformar:\n'))
d=s//(24*60*60)
s=s%(24*60*60)
h=s//(60*60)
s=s%(60*60)
m=s//60
s=s%60
print(d, "Dias", h, "horas", m, "minutos", s, "segundos")
