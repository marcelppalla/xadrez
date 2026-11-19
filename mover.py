from tabuleiro import tabuleiro
from validacoes import validacao

def mover(peca,linhaI,colunaI,linhaF,colunaF):
    if validacao(peca,linhaI,colunaI,linhaF,colunaF):
        #esvazia a posição de origem deixada
        tabuleiro[linhaI][colunaI]=" "
        #armazena a peca na posição destino
        tabuleiro[linhaF][colunaF]=peca
        #sinaliza que moveu
        return True
    return False