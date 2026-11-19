from validacoes import *
from mover import *
from tabuleiro import *

tabuleiro=criar_tabuleiro()

isNotOver=True

while isNotOver:
    mostrar_tabuleiro(tabuleiro)
    controlar_turno()

    i=input("Posição da peça a mover (linha,coluna): ").split(",")
    f=input("Posição de destino (linha,coluna): ").split(",")

    linhaI=int(i[0])
    colunaI=int(i[1])
    linhaF=int(f[0])
    colunaF=int(f[1])

    peca=tabuleiro[linhaI][colunaI]

    if mover(peca,linhaI,colunaI,linhaF,colunaF):
        trocar_turno()
    else:
        print("Jogada inválida!")

    