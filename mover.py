from tabuleiro import *
from validacoes import *

#conversão da entrada para os padroes do motrar_tabuleiro()
#coluna de letra para índices
def converter_coluna(coluna):
    match coluna.lower():
        case "a":
            return 0
        case "b":
            return 1
        case "c":
            return 2
        case "d":
            return 3
        case "e":
            return 4
        case "f":
            return 5
        case "g":
            return 6
        case "h":
            return 7
        case _:
            return -1

#linhas para os números corretos dos índices
def converter_linha(linha):
    return 8 - int(linha)

def mover(linhaIn,colunaIn,linhaFn,colunaFn):
    #conversão
        linhaI=converter_linha(linhaIn)
        linhaF=converter_linha(linhaFn)
        colunaI=converter_coluna(colunaIn)
        colunaF=converter_coluna(colunaFn)

        #se os parâmetros iniciais forem válidos (dentro dos limites do tabuleiro)
        if posicao_valida(linhaI,colunaI): 
            #define a peça
            peca=tabuleiro[linhaI][colunaI]
            #chama a validação geral
            if validacao(peca,linhaI,colunaI,linhaF,colunaF):
                #esvazia a posição de origem deixada
                tabuleiro[linhaI][colunaI]=" "
                #armazena a peca na posição destino
                tabuleiro[linhaF][colunaF]=peca
                #sinaliza que moveu
                return True
        return False