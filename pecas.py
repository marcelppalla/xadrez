from validacoes import *

#PEAO
#verifica se é o primeiro movimento do peão
def primeiro_mov(linhaI):
    if (controlar_turno()=="Brancas jogam" and linhaI==6) or ((controlar_turno()=="Pretas jogam" and linhaI==1)):
        return True
    return False 

def validacao_mov_peao(linhaI,colunaI,linhaF,colunaF):
    direcao=direcao_peca()
    #se o peao não se mexer no eixo horizontal
    if colunaI==colunaF:
        #se for o primeiro movimento do peão
        if primeiro_mov(linhaI):
            #pode andar até 1 ou 2 casas em sua direção
            if linhaF==(linhaI+2*direcao) or linhaF==(linhaI+direcao):
                return True
        #se não for o primeiro mov
        else:
            #só pode andar 1 casa em sua direção
            if linhaF==(linhaI+direcao):
               return True
        return False

def validacao_captura_peao(linhaI,colunaI,linhaF,colunaF):
    direcao=direcao_peca()
    #so pode andar 1 casa para frente
    if linhaF==(linhaI+direcao):
        #so pode ir 1 casa à direita ou esquerda
        if colunaF==(colunaI+1) or colunaF==(colunaI-1):
            return True
    return False

#TORRE
def validacao_mov_torre(linhaI, colunaI, linhaF, colunaF):
    #torre pode andar apenas em linha reta (mesma linha ou mesma coluna)
    if linhaI == linhaF or colunaI == colunaF:
        return True
    return Falses

#BISPO
def validacao_mov_bispo(linhaI, colunaI, linhaF, colunaF):
    # Define a direção do passo nas linhas (1 para baixo, -1 para cima)
    dir_linha = 0
    if linhaF > linhaI:
        dir_linha = 1
    elif linhaF < linhaI:
        dir_linha = -1

    # Define a direção do passo nas colunas (1 para direita, -1 para esquerda)
    dir_coluna = 0
    if colunaF > colunaI:
        dir_coluna = 1
    elif colunaF < colunaI:
        dir_coluna = -1

    # Precisa se mover nos dois eixos ao mesmo tempo e a mesma quantidade de casas
    if dir_linha != 0 and dir_coluna != 0:
        if (linhaF - linhaI) * dir_linha == (colunaF - colunaI) * dir_coluna:
            return True
    return False

#DAMA
def validacao_mov_dama(linhaI, colunaI, linhaF, colunaF):
    # A dama anda como torre (reto) ou como bispo (diagonal)
    if validacao_mov_torre(linhaI, colunaI, linhaF, colunaF) or validacao_mov_bispo(linhaI, colunaI, linhaF, colunaF):
        return True
    return False

#CAVALO
def validacao_mov_cavalo(linhaI, colunaI, linhaF, colunaF):
    # Anda 2 casas na vertical e 1 na horizontal
    if linhaF == (linhaI + 2) or linhaF == (linhaI - 2):
        if colunaF == (colunaI + 1) or colunaF == (colunaI - 1):
            return True

    # Anda 1 casa na vertical e 2 na horizontal
    if linhaF == (linhaI + 1) or linhaF == (linhaI - 1):
        if colunaF == (colunaI + 2) or colunaF == (colunaI - 2):
            return True

    return False

#REI
def validacao_mov_rei(linhaI, colunaI, linhaF, colunaF):
    # Verifica se o deslocamento na linha é de no máximo 1 passo
    passo_linha_valido = (linhaF == linhaI + 1) or (linhaF == linhaI - 1) or (linhaF == linhaI)
    # Verifica se o deslocamento na coluna é de no máximo 1 passo
    passo_coluna_valido = (colunaF == colunaI + 1) or (colunaF == colunaI - 1) or (colunaF == colunaI)

    if passo_linha_valido and passo_coluna_valido:
        return True
    return False
