kivansagLista = ['c64', 'ZX Spectrum']
mukodik = None
maxAr = 25000

tipus = input('milyen tipusu a gep?: ')
ar = int(input('mennyiert akarnad eladni?: '))
mukodes = input('mukodik a gep?(y/n): ')

if mukodes == 'y':
    mukodik = True
else:
    mukodik = False


if tipus in kivansagLista and ar <= maxAr and mukodik == True:
    print('megveszem a gepet!')
else:
    print('nem veszem meg a gepet!')