turno = input("Digite m para matutino, para v vesperino e n para noturno")

if turno == 'm' or turno == 'M':
    print("bom dia")
elif turno == 'v' or turno == 'V':
    print("boa tarde")
elif turno == 'n' or turno == 'N':
    print("boa noite")
else:
    print("Valor invalido")