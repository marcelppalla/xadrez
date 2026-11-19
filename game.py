from validacoes import *
from mover import *
from tabuleiro import *

while isNotOver(tabuleiro):
    mostrar_tabuleiro(tabuleiro)

    print()
    print(controlar_turno()+"!")
    print()

    try:
        i=input("Posição da peça a mover (linha,coluna): ").split(",")
        f=input("Posição de destino (linha,coluna): ").split(",")
        print()
    except ValueError:
        print("entrada inválida!")


    linhaI=i[0]
    colunaI=i[1]
    linhaF=f[0]
    colunaF=f[1]

    if mover(linhaI,colunaI,linhaF,colunaF):
        trocar_turno()
    else:
        print("Jogada inválida!")

    