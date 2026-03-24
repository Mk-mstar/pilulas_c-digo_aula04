def verificarNumero(x):
    if x % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
num = int(input('Digite o número: '))
retorno = verificarNumero(num) 
print(retorno)
