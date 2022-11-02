qtd_degraus = 0


def criar_degraus():
    qtd = 1
    degraus = ''
    while qtd <= qtd_degraus:
        print('⊞' *  qtd )
        qtd+=1
        
        
qtd_degraus = int(input('Número de degraus:'))
print(criar_degraus())