from validacoes import *
from mover import *
from tabuleiro import *

while reiVivo(tabuleiro):
    mostrar_capturadas(pretas_capturadas)
    print()
    mostrar_tabuleiro(tabuleiro)
    print()
    mostrar_capturadas(brancas_capturadas)
    print()
    print(controlar_turno()+"!")
    print()

    i=input("Posição da peça a mover (linha,coluna): ")
    f=input("Posição de destino (linha,coluna): ")
    print()

    linhaI=i[0]
    colunaI=i[1]
    linhaF=f[0]
    colunaF=f[1]
    
    if mover(linhaI,colunaI,linhaF,colunaF):
        trocar_turno()
    else:
        print("Jogada inválida!")