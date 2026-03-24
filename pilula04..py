try:
    
    pc = int(input('>>'))
    match pc : 
       case 1:
        print('Cadastrar')
       case 2:
        print('Alterar') 
       case 3: 
        print('Excluir')
       case 4: 
        print('Sair')
       case _:
        print('Valor errado') 
        
except:
    print('Digite algo certo')
            