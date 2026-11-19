from validacoes import *
from mover import *
from tabuleiro import *

tabuleiro=criar_tabuleiro()

isNotOver=True

while isNotOver:
    mostrar_tabuleiro(tabuleiro)
    controlar_turno()

    i=int(input("Posição da peça a mover (linha,coluna): ").split(","))
    f=int(input("Posição de destino (linha,coluna): ").split(","))

    linhaI=i[0]
    colunaI=i[1]
    linhaF=f[0]
    colunaF=f[1]

    peca=tabuleiro[linhaI][colunaI]

    if mover(peca,linhaI,colunaI,linhaF,colunaF):
        trocar_turno()
    else:
        print("Jogada inválida!")

    