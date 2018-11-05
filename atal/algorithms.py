#coding: utf-8

import sys

# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
    for j in xrange(len(alist)):
        for i in xrange(len(alist)-1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist

# Esse metodo recebe e valor para ser dado o troco e uma lista com os tipos de moedas possiveis
# e retorna o numero minimo de moedas possiveis em que o troco pode ser dado

# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda
def retorna_minimo_moedas(valor, tipos_moedas):
    print valor, tipos_moedas

    tipos_moedas.sort(reverse=True)

    resultado = retorna_minimo_moedas_Guloso(tipos_moedas, valor)

    return resultado

def retorna_minimo_moedas_Guloso(tipos_moedas, valor):
    soma = 0
    min_moedas = 0
    index_moeda = 0

    while (soma != valor):
        # esgotou todas as moedas da lista, logo, não há soluçao
        if (index_moeda == len(tipos_moedas)):
            return -1

        while (soma + tipos_moedas[index_moeda] <= valor): # pega a moeda o máximo de vezes possível
            soma = soma + tipos_moedas[index_moeda]
            min_moedas = min_moedas + 1

        index_moeda = index_moeda + 1

    return min_moedas



