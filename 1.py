def main():
    szamEgy = int(input('adja meg az elso szamot: '))
    szamKetto = int(input('adja meg a masodik szamot: '))
    muvelet = input('adja meg a muveletet: ')


    if muvelet == '+':
        print(f'{szamEgy} + {szamKetto} = {szamEgy + szamKetto}')
    elif muvelet == '-':
        print(f'{szamEgy} - {szamKetto} = {szamEgy - szamKetto}')
    elif muvelet == '*':
        print(f'{szamEgy} * {szamKetto} = {szamEgy * szamKetto}')
    elif muvelet == '/':    
        print(f'{szamEgy} / {szamKetto} = {szamEgy / szamKetto}')



while True:
    main()
    folyt = input('szeretne folytatni?(y/n): ')
    if folyt == 'n':
        quit()