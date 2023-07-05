def insercaoSimples(lista):
    n = len(lista)

    for j in range(1, n):
        chave = lista[j]
        i = j - 1

        while i >= 0 and lista[i] > chave:
            lista[i + 1] = lista[i]
            i = i - 1
        lista[i + 1] = chave