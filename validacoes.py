from tabuleiro import * 

def direcao_peca():
    turno=controlar_turno()
    #brancas sobem
    if turno=="Brancas jogam":
        return -1
    #pretas descem
    else:
        return 1

#não ficar na mesma posição
def sairInercia(linhaI, colunaI, linhaF, colunaF):
    if linhaI!=linhaF or colunaI!=colunaF:
        return True
    return False

#veririca se a posição de origem não está vazia
def posicao_nao_vazia(linhaI,colunaI):
    if tabuleiro[linhaI][colunaI]!=" ":
        return True
    return False

def posicao_valida(linha, coluna):
    """
    Verifica se a posição está dentro dos limites do tabuleiro.
    """
    if linha >= 0 and linha < 8 and coluna >= 0 and coluna < 8:
        return True
    return False

#rodada e controle de turno
rodada_atual=1

#incrementa a rodada
def trocar_turno():
    global rodada_atual
    rodada_atual+=1
    return rodada_atual

def controlar_turno():
    #se a rodada for par, será a vez das pretas
    if rodada_atual%2==0:
       return "Pretas jogam"
    #se for ímpar, brancas
    else:
       return "Brancas jogam"

#verifica se a peça é branca (maiúscula)
def eh_branca(peca):
    """
    Verifica se a peça pertence às brancas usando apenas comparação explícita de strings.
    """
    if peca == "P" or peca == "T" or peca == "C" or peca == "B" or peca == "D" or peca == "R":
        return True
    return False

#verifica se a cor da peça escolhida está condizente com a rodada
def validacao_cor(peca):
    turno=controlar_turno()
    if turno == "Brancas jogam":
        #se for branca
        if eh_branca(peca):
            return True
        #se for preta
        else:
            print("Peça inválida, rodada das brancas!")
            return False
    #se o turno for das pretas
    else:
        #se for preta
        if not eh_branca(peca):
            return True
        #se for branca
        else:
            print("Peça inválida, rodada das pretas!")
            return False

# validação específica do movimento de cada peça
def validacao_mov_peca(peca, linhaI, colunaI, linhaF, colunaF,captura=False):
    match peca:
        # retorna um boolean
        case "p":
            from pecas import validacao_mov_peao,validacao_captura_peao
            #peao possui validação específica de captura
            if captura:
                return validacao_captura_peao(linhaI,colunaI,linhaF,colunaF)
            return validacao_mov_peao(linhaI, colunaI, linhaF, colunaF)
        case "b":
            from pecas import validacao_mov_bispo
            return validacao_mov_bispo(linhaI, colunaI, linhaF, colunaF)
        case "c":
            from pecas import validacao_mov_cavalo
            return validacao_mov_cavalo(linhaI, colunaI, linhaF, colunaF)
        case "t":
            from pecas import validacao_mov_torre
            return validacao_mov_torre(linhaI, colunaI, linhaF, colunaF)
        case "r":
            from pecas import validacao_mov_rei
            return validacao_mov_rei(linhaI, colunaI, linhaF, colunaF)
        case "d":
            from pecas import validacao_mov_dama
            return validacao_mov_dama(linhaI, colunaI, linhaF, colunaF)

def cores_diferentes(atacante,adversaria):
    cor_atacante=eh_branca(atacante)
    cor_adversaria=eh_branca(adversaria)
    if cor_atacante!=cor_adversaria:
        return True
    return False

def caminho_livre(peca,linhaI,colunaI,linhaF,colunaF):
    #cavalo pula, não precisa verificar
    if peca == "c":
        return True
    #direção do passo
    dir_passo_linha=0

    #se a peca esta descendo
    if linhaI>linhaF:
        dir_passo_linha=-1
    #se a peca esta subindo
    elif linhaI<linhaF:
        dir_passo_linha=1

    dir_passo_coluna=0
     #se a peca esta indo para a direita
    if colunaI<colunaF:
        dir_passo_coluna=1
    #se a peca esta indo para a esquerda
    elif colunaI>colunaF:
        dir_passo_coluna=-1

    #começa a analisar a partir da próxima posição
    lin_atual=linhaI+dir_passo_linha
    col_atual=colunaI+dir_passo_coluna
    #percorre o caminho da peca ate o destino
    while (lin_atual!=linhaF) or (col_atual!=colunaF):
        #se o caminho não estiver livre retorna False
        if tabuleiro[lin_atual][col_atual]!=" ":
            return False
        #próxima casa
        lin_atual+=dir_passo_linha
        col_atual+=dir_passo_coluna
    return True

#linhaI: linha inicial
#linhaF: linha final
#colunaI: coluna inicial
#colunaF: coluna final
def validacao(peca,linhaI,colunaI,linhaF,colunaF):   
    #se os parâmetros finais forem válidos
    if posicao_valida(linhaF,colunaF):
        #se a pos de origem não estiver vazia
        if posicao_nao_vazia(linhaI,colunaI):
            #se sair da inercia
            if sairInercia(linhaI, colunaI, linhaF, colunaF):
                #se passar pela validação de cor
                if validacao_cor(peca):
                    peca=peca.lower()
                    pos_origem=tabuleiro[linhaI][colunaI]
                    pos_destino=tabuleiro[linhaF][colunaF]
                    #se o caminho estiver livre para avançar
                    if caminho_livre(peca,linhaI,colunaI,linhaF,colunaF):
                        #se houver uma peça na pos destino
                        if pos_destino!=" ":
                            #se forem de cores diferentes
                            if cores_diferentes(pos_origem,pos_destino):
                                #chama a função com captura=True
                                if validacao_mov_peca(peca,linhaI,colunaI,linhaF,colunaF,True):
                                        return True
                        #se não houver nenhuma peça no destino
                        else:
                            #validacao especifica de cada peca
                            if validacao_mov_peca(peca,linhaI,colunaI,linhaF,colunaF):
                                return True

#verifica a cada rodada se o jogo acabou (se há apenas um rei)
def reiVivo(tabuleiro):
    reis=[]
    count=0
    L = 0
    while L < len(tabuleiro):
        C = 0
        while C < len(tabuleiro[L]):
            peca=tabuleiro[L][C]
            #verifica se os dois reis estão em jogo
            if peca == "r" or peca=="R":
                reis.append(peca)
                count+=1
            C += 1
        L += 1
    #se apenas houver um, acabou o jogo
    if count<2:
        #mostra última rodada
        mostrar_tabuleiro(tabuleiro)
        print("Game Over")
        #verifica equipe vencedora pelo rei que sobrou
        if eh_branca(reis[0]):
            print("Brancas venceram!")
        else:
            print("Pretas venceram!") 
        return False
    return True

#implementar verificação do xeque matte