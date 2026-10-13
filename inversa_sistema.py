#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file    inversa_sistema.py
@brief   Determinação da inversa de uma matriz por escalonamento (Gauss-Jordan)
         e solução de sistemas lineares via matriz inversa (x = A^-1 * b).

@details Programa estrutural (sem classes), em um único arquivo.
         Fluxo:
           1. Lê a matriz A (n x n) e o vetor de termos independentes b.
           2. Monta a matriz aumentada [A | I].
           3. Escalona até obter [I | A^-1] (Gauss-Jordan com pivoteamento parcial).
           4. Calcula x = A^-1 * b.
           5. Verifica o resultado (A * A^-1 = I e A * x = b).

@author  khaos77
@date    2026
"""

## Tolerância numérica: valores menores que isso são tratados como zero.
EPS = 1e-12


# ----------------------------------------------------------------------------
# Funções de entrada e saída
# ----------------------------------------------------------------------------

def ler_matriz(n):
    """
    @brief  Lê uma matriz quadrada n x n do teclado, linha por linha.
    @param  n  Ordem da matriz.
    @return Matriz A como lista de listas de float.
    """
    print(f"\nDigite a matriz A ({n}x{n}), uma linha por vez, valores separados por espaço:")
    A = []
    for i in range(n):
        while True:
            try:
                linha = [float(v.replace(",", ".")) for v in input(f"  Linha {i + 1}: ").split()]
                if len(linha) != n:
                    print(f"  -> A linha deve ter exatamente {n} valores.")
                    continue
                A.append(linha)
                break
            except ValueError:
                print("  -> Entrada inválida. Use apenas números.")
    return A


def ler_vetor(n):
    """
    @brief  Lê o vetor de termos independentes b (n elementos).
    @param  n  Tamanho do vetor.
    @return Vetor b como lista de float.
    """
    while True:
        try:
            b = [float(v.replace(",", ".")) for v in
                 input(f"\nDigite o vetor b ({n} valores separados por espaço): ").split()]
            if len(b) == n:
                return b
            print(f"  -> O vetor deve ter exatamente {n} valores.")
        except ValueError:
            print("  -> Entrada inválida. Use apenas números.")


def imprimir_matriz(M, titulo="", separador=None):
    """
    @brief  Imprime uma matriz formatada no terminal.
    @param  M          Matriz (lista de listas).
    @param  titulo     Texto exibido acima da matriz.
    @param  separador  Índice de coluna onde desenhar a barra '|' (matriz aumentada).
                       Se None, nenhuma barra é desenhada.
    """
    if titulo:
        print(f"\n{titulo}")
    for linha in M:
        texto = ""
        for j, valor in enumerate(linha):
            if separador is not None and j == separador:
                texto += " |"
            # "+ 0.0" evita imprimir "-0.0000"
            texto += f" {valor + 0.0:9.4f}"
        print(texto)


# ----------------------------------------------------------------------------
# Funções de cálculo
# ----------------------------------------------------------------------------

def montar_matriz_aumentada(A):
    """
    @brief  Monta a matriz aumentada [A | I].
    @param  A  Matriz quadrada n x n.
    @return Matriz n x 2n, com A à esquerda e a identidade à direita.
    """
    n = len(A)
    return [A[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def inversa_por_escalonamento(A, passo_a_passo=False):
    """
    @brief  Calcula a inversa de A pelo método de Gauss-Jordan.
    @details Transforma [A | I] em [I | A^-1] por operações elementares:
             troca de linhas, normalização do pivô e eliminação nas demais linhas.
             Usa pivoteamento parcial (maior valor absoluto da coluna) para
             maior estabilidade numérica.
    @param  A              Matriz quadrada n x n.
    @param  passo_a_passo  Se True, imprime a matriz aumentada a cada etapa.
    @return A^-1 (lista de listas) ou None se A for singular (sem inversa).
    """
    n = len(A)
    M = montar_matriz_aumentada(A)

    if passo_a_passo:
        imprimir_matriz(M, "Matriz aumentada inicial [A | I]:", separador=n)

    for i in range(n):
        # 1) Pivoteamento parcial: acha a linha com maior |valor| na coluna i
        linha_pivo = max(range(i, n), key=lambda k: abs(M[k][i]))
        if abs(M[linha_pivo][i]) < EPS:
            return None  # pivô nulo -> det(A) = 0 -> matriz singular

        # 2) Troca a linha atual com a linha do pivô
        if linha_pivo != i:
            M[i], M[linha_pivo] = M[linha_pivo], M[i]
            if passo_a_passo:
                imprimir_matriz(M, f"Troca L{i + 1} <-> L{linha_pivo + 1}:", separador=n)

        # 3) Normaliza a linha do pivô (pivô passa a valer 1)
        pivo = M[i][i]
        M[i] = [valor / pivo for valor in M[i]]

        # 4) Zera a coluna i em todas as outras linhas
        for k in range(n):
            if k != i:
                fator = M[k][i]
                M[k] = [M[k][j] - fator * M[i][j] for j in range(2 * n)]

        if passo_a_passo:
            imprimir_matriz(M, f"Após zerar a coluna {i + 1}:", separador=n)

    # Metade direita da matriz aumentada é a inversa
    return [linha[n:] for linha in M]


def multiplicar_matriz_vetor(M, v):
    """
    @brief  Multiplica uma matriz por um vetor (M * v).
    @param  M  Matriz n x n.
    @param  v  Vetor de tamanho n.
    @return Vetor resultante de tamanho n.
    """
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def multiplicar_matrizes(A, B):
    """
    @brief  Multiplica duas matrizes quadradas (A * B).
    @param  A  Matriz n x n.
    @param  B  Matriz n x n.
    @return Matriz produto n x n.
    """
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def resolver_sistema_via_inversa(A_inv, b):
    """
    @brief  Resolve o sistema A x = b usando a inversa: x = A^-1 * b.
    @param  A_inv  Inversa de A.
    @param  b      Vetor de termos independentes.
    @return Vetor solução x.
    """
    return multiplicar_matriz_vetor(A_inv, b)


# ----------------------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------------------

def main():
    """
    @brief  Função principal: lê os dados, calcula a inversa, resolve o sistema
            e exibe a verificação dos resultados.
    """
    print("=" * 60)
    print(" INVERSA POR ESCALONAMENTO E SOLUÇÃO DE SISTEMA VIA INVERSA")
    print("=" * 60)

    # --- Entrada de dados ---
    while True:
        try:
            n = int(input("\nOrdem da matriz (n): "))
            if n >= 1:
                break
            print("  -> n deve ser maior ou igual a 1.")
        except ValueError:
            print("  -> Digite um número inteiro.")

    A = ler_matriz(n)
    b = ler_vetor(n)
    mostrar = input("\nMostrar passo a passo do escalonamento? (s/n): ").strip().lower() == "s"

    # --- Cálculo da inversa ---
    A_inv = inversa_por_escalonamento(A, passo_a_passo=mostrar)

    if A_inv is None:
        print("\nA matriz é SINGULAR (determinante = 0): não possui inversa.")
        print("Logo, o sistema não pode ser resolvido por este método.")
        return

    imprimir_matriz(A_inv, "Matriz inversa A^-1:")

    # --- Solução do sistema ---
    x = resolver_sistema_via_inversa(A_inv, b)
    print("\nSolução do sistema (x = A^-1 * b):")
    for i, valor in enumerate(x):
        print(f"  x{i + 1} = {valor + 0.0:.6f}")

    # --- Verificações ---
    imprimir_matriz(multiplicar_matrizes(A, A_inv), "Verificação A * A^-1 (deve ser a identidade):")
    print("\nVerificação A * x (deve ser igual a b):")
    Ax = multiplicar_matriz_vetor(A, x)
    for i in range(n):
        print(f"  Linha {i + 1}: A*x = {Ax[i] + 0.0:.6f}   |   b = {b[i]:.6f}")


## Ponto de entrada do programa
if __name__ == "__main__":
    main()
