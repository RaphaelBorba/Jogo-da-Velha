#Jogo da Velha para dois jogadores!!!
def jogada(jogo):
    while True:
        try:
            linha=int(input('Informe a linha 0 a 2: '))
            coluna=int(input('Informe a coluna 0 a 2: '))
            if linha in [0,1,2] and coluna in [0,1,2] and jogo[linha][coluna]=='-':
                break
            else:
                erro()
        except:
            erro1()
    return linha, coluna

def Jogo():
    jogo=[['-','-','-'],['-','-','-'],['-','-','-']]
    print('   0    1    2\n0{}\n1{}\n2{}'.format(jogo[0],jogo[1],jogo[2]))
    es()
    x=0
    while True:
        if '-' not in jogo[0] and '-' not in jogo[1] and '-' not in jogo[2]:
            print('EMPATE!!!')
            break
        print('Jogador {}'.format((x%2)+1))
        linha, coluna=jogada(jogo)
        if ((x%2)+1)==1:
              jogo[linha][coluna]='X'
        elif ((x%2)+1)==2:
              jogo[linha][coluna]='O'
        win=vitoria(jogo)
        if win==1:
            print('Jogador {} GANHOU!!!'.format((x%2)+1))
            break
        es()
        print('   0    1    2\n0{}\n1{}\n2{}'.format(jogo[0],jogo[1],jogo[2]))
        es()
        x+=1



def vitoria(jogo):
    # Horizontais O
    if jogo[0][0]=='O' and jogo[0][1]=='O' and jogo[0][2]=='O':
        return 1
    elif jogo[1][0]=='O' and jogo[1][1]=='O' and jogo[1][2]=='O':
        return 1
    elif jogo[2][0]=='O' and jogo[2][1]=='O' and jogo[2][2]=='O':
        return 1
    # Horizontais X
    elif jogo[0][0]=='X' and jogo[0][1]=='X' and jogo[0][2]=='X':
        return 1
    elif jogo[1][0]=='X' and jogo[1][1]=='X' and jogo[1][2]=='X':
        return 1
    elif jogo[2][0]=='X' and jogo[2][1]=='X' and jogo[2][2]=='X':
        return 1
    # Verticais O
    elif jogo[0][0]=='O' and jogo[1][0]=='O' and jogo[2][0]=='O':
        return 1
    elif jogo[0][1]=='O' and jogo[1][1]=='O' and jogo[2][1]=='O':
        return 1
    elif jogo[0][2]=='O' and jogo[1][2]=='O' and jogo[2][2]=='O':
        return 1
    # Verticais X
    elif jogo[0][0]=='X' and jogo[1][0]=='X' and jogo[2][0]=='X':
        return 1
    elif jogo[0][1]=='X' and jogo[1][1]=='X' and jogo[2][1]=='X':
        return 1
    elif jogo[0][2]=='X' and jogo[1][2]=='X' and jogo[2][2]=='X':
        return 1
    # Cruzadas O
    elif jogo[0][0]=='O' and jogo[1][1]=='O' and jogo[2][2]=='O':
        return 1
    elif jogo[0][2]=='O' and jogo[1][1]=='O' and jogo[2][0]=='O':
        return 1
    # Cruzadas X
    elif jogo[0][0]=='X' and jogo[1][1]=='X' and jogo[2][2]=='X':
        return 1
    elif jogo[0][2]=='X' and jogo[1][1]=='X' and jogo[2][0]=='X':
        return 1

def es():
    print('\n-----------------------\n')
def erro():
    print('ERRO!!! Esse local já foi preenchido')

def erro1():
    print('Apenas números!')
