
num = 0 
cont = 0
while True:
     n = int(input('>>>'))
     if n == 0:
       break
num = num + n
cont = cont + 1   

if cont <= 0: 
    print(f'Não temos média')
else:
    print(f'A média é {num / cont}')
