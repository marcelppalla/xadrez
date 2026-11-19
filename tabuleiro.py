def criar_tabuleiro():
    """
    Cria o tabuleiro 8x8 e posiciona todas as peças no estado inicial do jogo de xadrez.
    """
    tabuleiro = [
        [" ", " ", " ", " ", " ", " ", " ", " "]
        for i in range(8)
    ]

    # peças pretas 
    tabuleiro[0] = ["t", "c", "b", "d", "r", "b", "c", "t"]
    tabuleiro[1] = ["p", "p", "p", "p", "p", "p", "p", "p"]

    # peças brancas
    tabuleiro[6] = ["P", "P", "P", "P", "P", "P", "P", "P"]
    tabuleiro[7] = ["T", "C", "B", "D", "R", "B", "C", "T"]

    return tabuleiro

def mostrar_tabuleiro(tabuleiro):
    """
    Mostra o tabuleiro com as letras das colunas e os números das linhas.
    """
    print("\n    a   b   c   d   e   f   g   h")
    print("  +---+---+---+---+---+---+---+---+")

    for i in range(8):
        print(8 - i, end=" |")

        for j in range(8):
            print(f" {tabuleiro[i][j]} |", end="")

        print(f" {8 - i}")
        print("  +---+---+---+---+---+---+---+---+")

    print("\n    a   b   c   d   e   f   g   h")

def eh_branca(peca):
    """
    Verifica se a peça pertence às brancas usando apenas comparação explícita de strings.
    """
    if peca == "P" or peca == "T" or peca == "C" or peca == "B" or peca == "D" or peca == "R":
        return True
    return False

#variável global
tabuleiro=criar_tabuleiro()

if __name__ == "__main__":
    mostrar_tabuleiro(tabuleiro)