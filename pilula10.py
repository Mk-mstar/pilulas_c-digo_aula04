def classificar(idade):
   if idade < 12: 
       return 'Criança'
   elif idade <= 17:
       return 'Adolescente'
   else:
       return 'Adulto'
   
i = int(input('>>'))
print(f'Idade {i} - {classificar(i)}')