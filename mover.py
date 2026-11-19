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
    try:    
        return 8 - int(linha)
    except ValueError:
        letras=["a","b","c","d","e","f","g","h"]
        for j in range(len(letras)):
            if linha==letras[j]:
                print("A linha deve ser um número de 1 a 8")
                exit()

brancas_capturadas=[]
pretas_capturadas=[]
def armazenar_capturadas(capturada,brancas=brancas_capturadas,pretas=pretas_capturadas):
    if eh_branca(capturada):
        brancas.append(capturada)
    else:
        pretas.append(capturada)

def mostrar_capturadas(capturadas):
    for i in range(len(capturadas)):
        print(capturadas[i],end=" ")


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
                alvo=tabuleiro[linhaF][colunaF]
                #se houver uma peça na posição destino
                if alvo!=" ":
                    #armazena-a
                    armazenar_capturadas(alvo)
                #armazena a peca na posição destino
                tabuleiro[linhaF][colunaF]=peca
                #sinaliza que moveu
                return True
        return False

