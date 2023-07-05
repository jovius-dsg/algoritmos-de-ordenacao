def selecaoDireta(lista,n):
    for i in range(n):
        k = i
        menor = lista[i]
        for j in range(i+1,n):
            if (lista[j]<menor):
                k = j
                menor = lista[j]
        lista[k] = lista[i]
        lista[i] = menor