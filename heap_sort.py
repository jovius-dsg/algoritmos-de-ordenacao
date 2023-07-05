def heapify(lista, n, i):
    largest = i
    l = 2 * i + 1  
    r = 2 * i + 2 

    if l < n and lista[i] < lista[l]:
        largest = l

    if r < n and lista[largest] < lista[r]:
        largest = r

    if largest != i:
        lista[i],lista[largest] = lista[largest],lista[i]

        heapify(lista, n, largest)
  
def heapSort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
