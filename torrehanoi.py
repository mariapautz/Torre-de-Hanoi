
numero_movimentos = 0
quantidade_pecas = 0


def inicializar(quantidade_pecas): #função para definir com quantos discos o jogador ira jogar
    global numero_movimentos
    torres = [[], [], []]
    numero_movimentos = 0
    if quantidade_pecas == 3 or quantidade_pecas == 4 or quantidade_pecas == 5 or quantidade_pecas == 6 or quantidade_pecas == 7 or quantidade_pecas == 8:
        torres[0] = list(range(quantidade_pecas, 0, -1)) #adicionar a torre principal a quantidade de discos definida anteriormente
    else:
        print ("Voce inseriu um numero invalido")
        quantidade_pecas = int(input("Insira com quantas peças você deseja jogar, sabendo que o mínimo é 3 e o máximo é 8: "))
        return inicializar(quantidade_pecas) #executa a funcao inicializar
    return torres #printa as torres
    
    
def movimento(torres): #função para definir o movimentos das peças
    global numero_movimentos
    movimento_haste0 = int(input("Insira a haste em que a peca esta para movimentar esta localizada: ")) - 1 #-1 usado para printar a torre do maior numero para o menor
    movimento_haste = int(input("Insira a haste em que voce deseja colocar a sua peça: ")) - 1
    if (movimento_haste0 >= 0 and movimento_haste0 < 3) and (movimento_haste >= 0 and movimento_haste < 3):
        if (len(torres[movimento_haste]) == 0): #verifica se a torre esta vazia
            torres[movimento_haste].append(torres[movimento_haste0][-1]) #se estiver vazia adiciona o disco selecionado na torre escolhida anteriormente
            torres[movimento_haste0].pop() #retira o disco da torre onde o mesmo estava localizado anteriormente
            numero_movimentos += 1
        elif torres[movimento_haste0][-1] < torres[movimento_haste][-1]: #verifica se o disco da torre selecionada eh menor que o disco da torre que se quer adiconar o mesmo
            torres[movimento_haste].append(torres[movimento_haste0][-1]) #se for menor adiciona o disco selecionado na torre escolhida anteriormente
            torres[movimento_haste0].pop() #retira o disco selecionado da torre onde estava localizado
            numero_movimentos += 1
        else:
            print ("Este movimento não pode ser executado ") #ou seja, o disco eh maior que o ultimo disco da torre onde se quer adiciona-lo
            movimento(torres)
    
    else:
        print ("Este movimento não pode ser executado ")
        movimento(torres)
    
def ganhador(torre3): #funcao para definir ganhador
    if len(torre3) == quantidade_pecas: #verifica se a torre inicial se iguala a torre final
        print ("Parabéns! Você acabou o jogo com " + str(numero_movimentos) + " movimentos") #mostra com quantos movimentos o jogador realizou o jogo
        equacao = (2 ** quantidade_pecas) -1 #calcula a quantidade minima de movimentos necessarios para concluir o jogo
        print ("O numero de movimentos minimos para executar eram " + str(equacao))
        return True
    return False

def printar_torres(torres): #funcao utilizada para printar o tabuleiro
    for i in range(8,0,-1): 
        torreesquerda = 0
        torremeio = 0
        torredireita = 0
        if len(torres[0]) >= i:
            torreesquerda = torres[0][i-1]
        if len(torres[1]) >= i:
            torremeio = torres[1][i-1]
        if len(torres[2]) >= i:
            torredireita = torres[2][i-1]
        print ('{:^20}'        '{:^20}'        '{:^20}'.format((torreesquerda*2)*'♥',(torremeio*2)*'♥',(torredireita*2)*'♥')) #printa as torres

quantidade_pecas = int(input("Insira com quantas peças você deseja jogar, sabendo que o mínimo é 3 e o máximo é 8: "))
torres = inicializar(quantidade_pecas)
rodando = True
while rodando: #roda o jogo
    printar_torres(torres)
    movimento(torres)
    if ganhador(torres[2]): #condiçao que verifica se a torre final esta correta
        jogar_novamente = input("Deseja jogar novamente(s/N): ")
        if jogar_novamente == 's': #condicao que verifica se o jogo sera executado novamente
            quantidade_pecas = int(input("Insira com quantas peças você deseja jogar, sabendo que o mínimo é 3 e o máximo é 8: "))
            torres = inicializar(quantidade_pecas)
        else: rodando = False
else:
    print("Espero que tenha gostado! ") #mensagem que para finalizar o jogo ^^

   


    

    

