# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem DECRESCENTE de matriculas
def retorna_matriculas_decrescente(alist):
	quick(alist, 0, len(alist) -1)
	return alist

def quick(lista, inicio, fim):
	if inicio < fim:
		pivot = partition(lista, inicio, fim)

		quick(lista, inicio, pivot - 1)
		quick(lista, pivot + 1, fim)

def partition(lista, inicio, fim):
	pivot = lista[inicio]
	index = inicio

	for i in range(inicio + 1, fim + 1):
		if lista[i] > pivot:
			index += 1
			lista[index], lista[i] = lista[i], lista[index]

	lista[inicio], lista[index] = lista[index], lista[inicio]

	return index
