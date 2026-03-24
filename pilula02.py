nota = float(input('Nota'))
freq = float(input('Freq'))

if freq < 75:
    print('Reprovado por falta')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('AF')
    
else: 
    print('Reprovado')
    