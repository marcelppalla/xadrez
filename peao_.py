from validacoes import *

#verifica se é o primeiro movimento do peão
def primeiro_mov(linhaI):
    if (controlar_turno()=="Brancas jogam" and linhaI==6) or ((controlar_turno()=="Brancas jogam" and linhaI==6)):
        return True
    return False 

def validacao_mov_peao(linhaI,linhaF):
    direcao=direcao_peca()
    #se for o primeiro movimento do peão
    if primeiro_mov(linhaI):
        #pode andar até 2 casas em sua direção
        if linhaF<(linhaI+3*direcao):
            return True
    #se não for o primeiro mov
    else:
        #pode andar até 1 casa em sua direção
        if linhaF<(linhaI+2*direcao):
            return True
    return False

def validacao_captura_peao(linhaI,colunaI,linhaF,colunaF):
    direcao=direcao_peca()
    #so pode andar 1 casa para frente
    if linhaF<(linhaI+2*direcao):
        #so pode ir 1 casa à direita ou esquerda
        if colunaF<(colunaI-2) or colunaF<(colunaI-2):
            return True
    return False


