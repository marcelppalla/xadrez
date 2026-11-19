from tabuleiro import tabuleiro

def direcao_peca():
    turno=controlar_turno()
    #brancas sobem
    if turno=="Brancas jogam":
        return 1
    #pretas descem
    else:
        return -1

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

def validacao_mov_peca(peca, linhaI, colunaI, linhaF, colunaF):
    from peao_ import validacao_mov_peao
    from bispo import validacao_mov_bispo
    from cavalo import validacao_mov_cavalo
    from torre import validacao_mov_torre
    from rei import validacao_mov_rei
    from dama import validacao_mov_dama

    match peca:
        # retorna um boolean
        case "p":
            return validacao_mov_peao(linhaI, colunaI, linhaF, colunaF)
        case "b":
            return validacao_mov_bispo(linhaI, colunaI, linhaF, colunaF)
        case "c":
            return validacao_mov_cavalo(linhaI, colunaI, linhaF, colunaF)
        case "t":
            return validacao_mov_torre(linhaI, colunaI, linhaF, colunaF)
        case "r":
            return validacao_mov_rei(linhaI, colunaI, linhaF, colunaF)
        case "d":
            return validacao_mov_dama(linhaI, colunaI, linhaF, colunaF)


def validacao_captura_peca(peca, linhaI, colunaI, linhaF, colunaF):
    from peao_ import validacao_captura_peao
    from bispo import validacao_captura_bispo
    from cavalo import validacao_captura_cavalo
    from torre import validacao_captura_torre
    from rei import validacao_captura_rei
    from dama import validacao_captura_dama

    match peca:
        # retorna um boolean
        case "p":
            return validacao_captura_peao(linhaI, colunaI, linhaF, colunaF)
        case "b":
            return validacao_captura_bispo(linhaI, colunaI, linhaF, colunaF)
        case "c":
            return validacao_captura_cavalo(linhaI, colunaI, linhaF, colunaF)
        case "t":
            return validacao_captura_torre(linhaI, colunaI, linhaF, colunaF)
        case "r":
            return validacao_captura_rei(linhaI, colunaI, linhaF, colunaF)
        case "d":
            return validacao_captura_dama(linhaI, colunaI, linhaF, colunaF)

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
        dir_passo_col=-1
    #se a peca esta indo para a esquerda
    elif colunaI>colunaF:
        dir_passo_col=1

    #começa a analisar a partir da próxima posição
    lin_atual=linhaI+dir_passo_linha
    col_atual=colunaI+dir_passo_col
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
    #se os parâmetros iniciais forem válidos (dentro dos limites do tabuleiro)
    if posicao_valida(linhaI,colunaI):    
        #se os parâmetros finais forem válidos
        if posicao_valida(linhaF,colunaF):
            #se passar pela validação de cor
            if validacao_cor(peca):
                peca=peca.lower()
                pos_origem=tabuleiro[linhaI][colunaI]
                pos_destino=tabuleiro[linhaF][colunaF]
                #se houver uma peça na pos destino      
                if pos_destino!=" ":       
                    atacante=pos_origem
                    adversaria=pos_destino
                    #se forem de cores diferentes
                    if cores_diferentes(atacante,adversaria):
                        #validacao de captura de cada peca
                        if validacao_captura_peca(peca,linhaI,colunaI,linhaF,colunaF):
                            return True
                else:
                    #se o caminho estiver livre para avançar
                    if caminho_livre(peca,linhaI,colunaI,linhaF,colunaF):
                        #validacao especifica de cada peca
                        if validacao_mov_peca(peca,linhaI,colunaI,linhaF,colunaF):
                            return True

#verifica a cada rodada se o jogo acabou (se há apenas uma peca)
def verificaSeAcabou(tabuleiro):
    pecas=[]
    count=0
    L = 0
    while L < len(tabuleiro):
        C = 0
        while C < len(tabuleiro[L]):
            peca=tabuleiro[L][C]
            if peca != " ":
                count+=1
                #armazena as pecas que ainda estão no jogo
                pecas.append(peca)
                #se há mais de uma peca, o jogo ainda não acabou, pode para o loop
                if count>2:
                    break
            C += 1
        L += 1
    #game over
    if count==1:
        print("Game Over")
        isNotOver=False
    #verifica equipe vencedora pela peca que sobrou
    if eh_branca(pecas[0]):
        print("Brancas venceram!")
    else:
        print("Brancas venceram!")

#implementar verificação do xeque matte
                

        

