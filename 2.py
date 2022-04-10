nev = input('adja meg az osember nevet: ')
bogyok = int(input('adja meg a gyujtott bogyok szamat: '))

if bogyok < 10:
    print(f'{nev} {bogyok} darab bogyot hozott igy zseneg minositest kap')
if bogyok > 20:
    print(f'{nev} {bogyok} darab bogyot hozott igy nagy koponya minositest kap')
if bogyok > 10 and bogyok < 20:
    print(f'{nev} {bogyok} darab bogyot hozott igy gyujtogeto minositest kap')