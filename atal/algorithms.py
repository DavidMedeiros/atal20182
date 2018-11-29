#coding: utf-8

import sys
# Mochila Binaria interativo

# Retorna o valor maximo que cabe na mochila com
# capacidade peso_maximo
def mochila_binaria(peso_maximo, pesos, valores, n):
    v = [[0] * (peso_maximo + 1) for _ in range(n + 1)]

    for i in range(1, len(v)):
        for j in range(1, len(v[i])):
            if pesos[i-1] > j:
                v[i][j] = v[i-1][j]
            else:
                v[i][j] = max(v[i-1][j - pesos[i-1]] + valores[i-1], v[i-1][j])

    return v[n][peso_maximo]